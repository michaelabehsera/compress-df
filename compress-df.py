import pandas as pd
def compress(df):
    mem = df.memory_usage().sum()
    print(f'Memory usage before conversion {mem}')

    ints = ['int16', 'int32', 'int64']

    def negative_compress():
        for col in df.columns:
            if df[col].dtypes in ints:
                for val in df[col]:
                    if val > -128 and val < 127:
                        df[col] = df[col].astype('int8')
                    elif val > -32768 and val < 32767:
                        df[col] = df[col].astype('int16')

    def natural_compress():
        for col in df.columns:
            if df[col].dtypes in ints:
                for val in df[col]:
                    if val > 0 and val < 255:
                        df[col] = df[col].astype('uint8')
                    elif val > 0 and val < 65535:
                        df[col] = df[col].astype('uint16')
                    elif val > 0 and val < 4294967295:
                        df[col] = df[col].astype('uint32')
                    elif val > 0 and val < 18446744073709551615:
                        df[col] = df[col].astype('uint64')

    result = None
    for col in df.columns:
        if df[col].dtypes in ints:
            for val in df[col]:
                if val > 0:
                    result = natural_compress()
                if val < 0:
                    result = negative_compress()

    memory_new = df.memory_usage().sum()
    print(f'Memory Usage After Conversion is {memory_new} and You Reduced the Memory by {memory_new / mem * 100}%! Good Job :)')
    print('Tip: If there are NaN values in one of the integer columns then make sure to replace the \nNaN values, sometimes becuase of the NaN value the column even though it has no floats \nwill be of a float dtype.')
    return result
