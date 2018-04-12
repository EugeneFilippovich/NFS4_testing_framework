from main_files import main_cases


class Assertion(object):

    @staticmethod
    def assert_change_folder(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully '.format(steps_quantity))
            class_name.logger.info('Directory has been changed ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_working_dir(class_name):
        class_name.logger.info(main_cases.MainCases.pwd())

    @staticmethod
    def assert_list_of_files(class_name):
        class_name.logger.info(main_cases.MainCases.ls())

    @staticmethod
    def assert_make_dir(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The directory has been created successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_remove_folder(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The folder has been removed successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_touch_file(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully '.format(steps_quantity))
            class_name.logger.info('File has been created successfully')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.info(step)

    @staticmethod
    def assert_write_into_file(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The file has been updated successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_read_file(class_name, file_name):
        class_name.logger.info('Data inside file: {}'.format(main_cases.MainCases.read_file(file_name)))

    @staticmethod
    def assert_cat_file(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('File is viewed by using {} '.format('cat'))
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_copy_file(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The file has been copied successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_move_file(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The file has been moved successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_rename_file(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The file has been renamed successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_remove_file(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The file has been removed successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_run_script(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('The file has been executed successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)

    @staticmethod
    def assert_ssh_to_server(step, class_name, steps_quantity):
        if not step:
            class_name.logger.debug('Step {} passed successfully'.format(steps_quantity))
            class_name.logger.info('Remote command has been executed successfully ')
        else:
            class_name.logger.debug('Step {} failed '.format(steps_quantity))
            class_name.logger.error(step)








