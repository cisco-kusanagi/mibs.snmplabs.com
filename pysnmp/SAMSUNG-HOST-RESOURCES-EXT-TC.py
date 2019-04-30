#
# PySNMP MIB module SAMSUNG-HOST-RESOURCES-EXT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-HOST-RESOURCES-EXT-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Integer32, Gauge32, IpAddress, Bits, ModuleIdentity, Counter32, Unsigned32, iso, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Integer32", "Gauge32", "IpAddress", "Bits", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scmHrTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52))
if mibBuilder.loadTexts: scmHrTC.setLastUpdated('0407170000Z')
if mibBuilder.loadTexts: scmHrTC.setOrganization('Samsung Corporation - SCMI Working Group')
scmHrDeviceTypes = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2))
if mibBuilder.loadTexts: scmHrDeviceTypes.setStatus('current')
scmHrDeviceHostSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 101))
if mibBuilder.loadTexts: scmHrDeviceHostSystem.setStatus('current')
scmHrDeviceScanner = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 102))
if mibBuilder.loadTexts: scmHrDeviceScanner.setStatus('current')
scmHrDeviceCopier = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 103))
if mibBuilder.loadTexts: scmHrDeviceCopier.setStatus('current')
scmHrDeviceFax = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 104))
if mibBuilder.loadTexts: scmHrDeviceFax.setStatus('current')
scmHrDeviceMailbox = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 105))
if mibBuilder.loadTexts: scmHrDeviceMailbox.setStatus('current')
scmHrDeviceFinisher = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 106))
if mibBuilder.loadTexts: scmHrDeviceFinisher.setStatus('current')
scmHrDeviceFeeder = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 107))
if mibBuilder.loadTexts: scmHrDeviceFeeder.setStatus('current')
scmHrDeviceSorter = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 108))
if mibBuilder.loadTexts: scmHrDeviceSorter.setStatus('current')
scmHrDeviceMailboxSorter = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 109))
if mibBuilder.loadTexts: scmHrDeviceMailboxSorter.setStatus('current')
scmHrDevicePrintAppliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 110))
if mibBuilder.loadTexts: scmHrDevicePrintAppliance.setStatus('current')
scmHrDeviceMarker = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 111))
if mibBuilder.loadTexts: scmHrDeviceMarker.setStatus('current')
scmHrDeviceFinisherBFM = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 112))
if mibBuilder.loadTexts: scmHrDeviceFinisherBFM.setStatus('current')
scmHrDeviceFinisherMFF = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 113))
if mibBuilder.loadTexts: scmHrDeviceFinisherMFF.setStatus('current')
scmHrDeviceFinisherXIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 114))
if mibBuilder.loadTexts: scmHrDeviceFinisherXIM.setStatus('current')
scmHrDeviceFinisher3rdParty = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 115))
if mibBuilder.loadTexts: scmHrDeviceFinisher3rdParty.setStatus('current')
scmHrDevicePaymentInterface = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 116))
if mibBuilder.loadTexts: scmHrDevicePaymentInterface.setStatus('current')
scmHrDeviceInterposer = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 117))
if mibBuilder.loadTexts: scmHrDeviceInterposer.setStatus('current')
scmHrDeviceHostSystemHistory = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 151))
if mibBuilder.loadTexts: scmHrDeviceHostSystemHistory.setStatus('current')
scmHrDeviceScannerHistory = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 152))
if mibBuilder.loadTexts: scmHrDeviceScannerHistory.setStatus('current')
scmHrDeviceCopierHistory = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 153))
if mibBuilder.loadTexts: scmHrDeviceCopierHistory.setStatus('current')
scmHrDeviceFaxHistory = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 154))
if mibBuilder.loadTexts: scmHrDeviceFaxHistory.setStatus('current')
scmHrDevicePrinterHistory = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 55))
if mibBuilder.loadTexts: scmHrDevicePrinterHistory.setStatus('current')
scmHrCruXerographicModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 201))
if mibBuilder.loadTexts: scmHrCruXerographicModule.setStatus('current')
scmHrCruFuserModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 202))
if mibBuilder.loadTexts: scmHrCruFuserModule.setStatus('current')
scmHrCruTonerBottleModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 203))
if mibBuilder.loadTexts: scmHrCruTonerBottleModule.setStatus('current')
scmHrCruCollectorBottleModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 204))
if mibBuilder.loadTexts: scmHrCruCollectorBottleModule.setStatus('current')
scmHrCruTrayFeedHeadModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 205))
if mibBuilder.loadTexts: scmHrCruTrayFeedHeadModule.setStatus('current')
scmHrCruAdfFeedHeadModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 206))
if mibBuilder.loadTexts: scmHrCruAdfFeedHeadModule.setStatus('current')
scmHrCruFuserWebModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 207))
if mibBuilder.loadTexts: scmHrCruFuserWebModule.setStatus('current')
scmHrCruFilterModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 208))
if mibBuilder.loadTexts: scmHrCruFilterModule.setStatus('current')
scmHrCruCleanerUnitModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 209))
if mibBuilder.loadTexts: scmHrCruCleanerUnitModule.setStatus('current')
scmHrCruTransferUnitModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 210))
if mibBuilder.loadTexts: scmHrCruTransferUnitModule.setStatus('current')
scmHrCruTransferRollerModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 211))
if mibBuilder.loadTexts: scmHrCruTransferRollerModule.setStatus('current')
scmHrCruPFPFeedRollModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 212))
if mibBuilder.loadTexts: scmHrCruPFPFeedRollModule.setStatus('current')
scmHrCruPFPRetardRollModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 213))
if mibBuilder.loadTexts: scmHrCruPFPRetardRollModule.setStatus('current')
scmHrDeviceUSBPort = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 250))
if mibBuilder.loadTexts: scmHrDeviceUSBPort.setStatus('current')
scmHrDeviceFlashDIMMFileStore = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 260))
if mibBuilder.loadTexts: scmHrDeviceFlashDIMMFileStore.setStatus('current')
scmHrDeviceFlashDIMMBootLoader = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 261))
if mibBuilder.loadTexts: scmHrDeviceFlashDIMMBootLoader.setStatus('current')
scmHrAdminServiceTypes = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3))
if mibBuilder.loadTexts: scmHrAdminServiceTypes.setStatus('current')
scmHrAdminObjectService = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 1))
if mibBuilder.loadTexts: scmHrAdminObjectService.setStatus('current')
scmHrAdminServerService = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 2))
if mibBuilder.loadTexts: scmHrAdminServerService.setStatus('current')
scmHrAdminDeviceService = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 3))
if mibBuilder.loadTexts: scmHrAdminDeviceService.setStatus('current')
scmHrAdminJobService = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 4))
if mibBuilder.loadTexts: scmHrAdminJobService.setStatus('current')
scmHrAdminDocService = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 5))
if mibBuilder.loadTexts: scmHrAdminDocService.setStatus('current')
scmHrAdminSecurityService = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 6))
if mibBuilder.loadTexts: scmHrAdminSecurityService.setStatus('current')
scmHrAdminCommsService = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 7))
if mibBuilder.loadTexts: scmHrAdminCommsService.setStatus('current')
scmHrAdminDeviceOperationTypes = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4))
if mibBuilder.loadTexts: scmHrAdminDeviceOperationTypes.setStatus('current')
scmHrAdminDeviceNone = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 1))
scmHrAdminDeviceStartup = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 2))
scmHrAdminDeviceResetWarning = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 3))
scmHrAdminDeviceTest = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 4))
scmHrAdminDeviceShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 5))
scmHrAdminDeviceQuiesce = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 6))
scmHrAdminDeviceResetCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 7))
scmHrAdminDeviceResetWarm = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 8))
scmHrAdminDeviceResetCold = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 9))
scmHrAdminDeviceResetFactory = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 10))
scmHrAdminDeviceFlushInput = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 11))
scmHrAdminDeviceFlushOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 12))
scmHrAdminDeviceFlushInOut = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 13))
scmHrAdminDeviceManage = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 14))
scmHrAdminDeviceRefresh = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 15))
scmHrAdminDeviceWarmUp = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 16))
scmHrAdminDeviceCoolDown = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 17))
scmHrAdminDeviceEnergySave = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 18))
scmHrAdminDeviceWakeUp = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 19))
scmHrAdminDevicePowerToReady = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 20))
scmHrAdminDevicePowerToStandby = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 21))
scmHrAdminDevicePowerToSleep = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 22))
class ScmHrDevCalendarDayOfWeek(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("everyDay", 8), ("businessOpenDay", 9), ("businessClosedDay", 10), ("businessHoliday", 11))

class ScmHrDevCalendarTimeOfDay(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(10000, 12359)

class ScmHrDevDetailType(TextualConvention, Integer32):
    reference = "See: 'scmHrDevDetailUnitClass' and 'scmHrDevDetailUnit' for syntax of device detail."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 41, 42, 43, 44, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 130, 140, 160, 161, 162, 163, 191, 192, 193, 194, 200, 201, 202, 203, 204, 210, 211, 212, 213, 220, 221, 230, 231, 232))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("deviceName", 3), ("deviceAlias", 4), ("deviceType", 5), ("deviceDescription", 6), ("deviceID", 7), ("deviceTree", 8), ("deviceContext", 9), ("deviceManufacturer", 10), ("deviceModel", 11), ("deviceSerialNumber", 12), ("deviceVendor", 13), ("deviceVersion", 14), ("deviceServiceByCustomer", 15), ("deviceReplaceByCustomer", 16), ("deviceServicePlanName", 17), ("deviceServicePlanPassword", 18), ("deviceReplaceByWarranty", 19), ("deviceLifetimeUsage", 20), ("deviceReorderLifetimeLimit", 21), ("deviceWarningLifetimeLimit", 22), ("deviceReplaceLifetimeLimit", 23), ("deviceMaximumLifetimeLimit", 24), ("deviceDaysUntilReorderMsg", 25), ("deviceDaysUntilWarningMsg", 26), ("deviceDaysUntilReplaceMsg", 27), ("deviceDaysUntilMaximumMsg", 28), ("deviceLifetimeMsgDisplay", 29), ("deviceAccountingUsage", 30), ("deviceReorderOnDate", 31), ("deviceWarningOnDate", 32), ("deviceReplaceOnDate", 33), ("deviceMaximumOnDate", 34), ("deviceLifetimeErrorCount", 35), ("deviceLifetimeErrorLimit", 36), ("deviceLifetimeWarningCount", 37), ("deviceLifetimeWarningLimit", 38), ("deviceTriggerDaysForReorder", 41), ("deviceTriggerDaysForWarning", 42), ("deviceTriggerDaysForReplace", 43), ("deviceTriggerDaysForMaximum", 44), ("deviceReorderMsgSentDate", 51), ("deviceWarningMsgSentDate", 52), ("deviceReplaceMsgSentDate", 53), ("deviceMaximumMsgSentDate", 54), ("deviceReorderToVendorDate", 55), ("deviceReorderConfirmDate", 56), ("deviceReplaceDate", 57), ("deviceReplaceSystemUsage", 58), ("deviceReplaceWithGeneric", 59), ("deviceHelpName", 60), ("deviceHelpAddress", 61), ("deviceHelpDescription", 62), ("deviceHelpLocation", 63), ("deviceHelpURI", 64), ("deviceTranslatorSupport", 71), ("deviceTranslatorReady", 72), ("deviceInitialValueJobSupport", 73), ("deviceInitialValueDocSupport", 74), ("deviceMultipleDocSupport", 75), ("deviceCancelDocSupport", 76), ("deviceForeignJobsVisible", 77), ("deviceInitialValueJobDefault", 78), ("deviceInitialValueDocDefault", 79), ("deviceInputMaxSpeedTrafficUnit", 80), ("deviceInputMaxSpeedTimeUnit", 81), ("deviceInputMaxSpeed", 82), ("deviceOutputMaxSpeedTrafficUnit", 83), ("deviceOutputMaxSpeedTimeUnit", 84), ("deviceOutputMaxSpeed", 85), ("deviceFeedResolutionSupport", 86), ("deviceXFeedResolutionSupport", 87), ("deviceSchedulerSupport", 88), ("deviceSchedulerReady", 89), ("devicePhysicalNameSupport", 90), ("devicePhysicalNameReady", 91), ("deviceLogicalNameSupport", 92), ("deviceLogicalNameReady", 93), ("devicePhysicalIndexSupport", 94), ("devicePhysicalIndexReady", 95), ("deviceLogicalIndexSupport", 96), ("deviceLogicalIndexReady", 97), ("deviceJobServiceDeviceIndex", 98), ("deviceJobHistoryDeviceIndex", 99), ("deviceFontIndexSupport", 100), ("deviceFontIndexReady", 101), ("deviceResourceIndexSupport", 102), ("deviceResourceIndexReady", 103), ("devicePowerModeName", 110), ("devicePowerModeType", 111), ("devicePowerModeDescription", 112), ("devicePowerModeSupport", 113), ("devicePowerTimeUnit", 114), ("devicePowerWarmerSupport", 115), ("devicePowerCoolerSupport", 116), ("devicePowerWarmerDelay", 117), ("devicePowerWarmerDuration", 118), ("devicePowerCoolerDelay", 119), ("devicePowerCoolerDuration", 120), ("devicePowerWarmerTrigger", 121), ("devicePowerCoolerTrigger", 122), ("deviceNextWarmerModeIndex", 123), ("deviceNextCoolerModeIndex", 124), ("deviceEnergyStarSuspendMode", 125), ("deviceProcessorFrwID", 130), ("deviceNetworkIfIndex", 140), ("deviceDiskStorageAccess", 160), ("deviceDiskStorageMedia", 161), ("deviceDiskStorageRemovable", 162), ("deviceDiskStorageCapacity", 163), ("deviceJobIncompleteTimeout", 191), ("deviceJobProgrammingTimeout", 192), ("deviceJobHoldDeleteTimeout", 193), ("deviceJobPauseResumeTimeout", 194), ("deviceGuestJobPolicy", 200), ("deviceAlienJobPolicy", 201), ("deviceEventLogFullPolicy", 202), ("deviceJobLogFullPolicy", 203), ("deviceRequestLogFullPolicy", 204), ("deviceUniversalProductCode", 210), ("deviceModelName", 211), ("deviceModelDescription", 212), ("deviceModelNumber", 213), ("deviceManufacturerURI", 220), ("deviceModelURI", 221), ("deviceServiceUsage", 230), ("deviceDeltaServiceUsage", 231), ("deviceRolloverValue", 232))

class ScmHrDevDetailUnitClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("classGenOptionValueSyntax", 3), ("classDateAndTime", 4), ("classHrDevCalendarDayOfWeek", 5), ("classHrDevCalendarTimeOfDay", 6), ("classHrDevMgmtCommandRequest", 7), ("classHrDevPowerTimeUnit", 8), ("classHrDevTrafficUnit", 9), ("classRowPersistence", 10), ("classRowPersistenceMask", 11), ("classLogFullPolicy", 12), ("classLogFullPolicyMask", 13), ("classHrDevInfoStatus", 14), ("classHrDevInfoStatusMask", 15), ("classHrDevInfoXStatus", 16), ("classHrDpaState", 17), ("classHrDpaConditions", 18), ("classHrDpaAvailability", 19), ("classHrDpaObjectClassSupport", 20), ("classHrDpaJobValidateSupport", 21), ("classJMJobState", 22), ("classJMJobStateMask", 23), ("classSecGuestJobPolicy", 24), ("classSecGuestJobPolicyMask", 25), ("classSecPosixRights", 26), ("classSecPosixVerbs", 27), ("classSvcMonJobConfirmSupport", 28), ("classSvcMonAttachmentPDLSupport", 29))

class ScmHrDevInfoRealization(TextualConvention, Integer32):
    reference = "See: 'hrDeviceType' in the basic Device Group of the IETF Host Resources MIB (RFC 2790). See: Section 9.4 'Printer Object attributes' of ISO DPA (Document Printing Application) ISO/IEC 10175 (Final Text, March 1996) for a discussion of 'printer realizations' of 'physical', 'logical', and 'logical-and-physical' types (the latter unique to DPA)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("physical", 11), ("logical", 12), ("logicalAndPhysical", 13))

class ScmHrDevInfoStatus(TextualConvention, Integer32):
    reference = "See: 'hrDeviceStatus' in the basic Device Group of the IETF Host Resources MIB (RFC 2790). See: 'scmHrDevInfoXStatus', 'scmHrDevInfoConditions', and 'scmHrDevInfoXConditions' in the Host Resources Extensions MIB."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("running", 2), ("warning", 3), ("testing", 4), ("down", 5))

class ScmHrDevInfoXStatus(TextualConvention, Integer32):
    reference = "See: Section 9.4.9 'Printer-state' of ISO DPA (Document Printing Application) ISO/IEC 10175 (Final Text, 18 May 1995) for a discussion of the printer states used here. Note that the DPA state 'connecting-to-printer' has no meaning in the context of a 'physical' printer device, but only in the context of an intermediate DP-Server presenting a 'logical' printer device. See: 'hrPrinterStatus' and 'hrPrinterDetectedErrorState' in the IETF Host Resources MIB (RFC 2790) for related discussion. See: 'hrDeviceStatus' in the basic Device Group of the IETF Host Resources MIB (RFC 2790). See: 'scmHrDevInfoConditions' and 'scmHrDevInfoXConditions' in the Host Resources Extensions MIB."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 99, 100, 200, 300, 400, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 600, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 10100, 10200, 10300, 10400, 10500, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 20000, 20001, 20002, 20003, 20004, 20005, 20006, 40000))
    namedValues = NamedValues(("commonNone", 0), ("commonOther", 1), ("commonUnknown", 2), ("commonLast", 99), ("otherNone", 100), ("unknownNone", 200), ("processorNone", 300), ("networkNone", 400), ("printerNone", 500), ("printerOther", 501), ("printerUnknown", 502), ("printerIdle", 503), ("printerPrinting", 504), ("printerNeedsAttention", 505), ("printerPaused", 506), ("printerShutdown", 507), ("printerJobStartWait", 508), ("printerJobEndWait", 509), ("printerNeedsKeyOperator", 510), ("printerJobPasswordWait", 511), ("printerTimedOut", 512), ("printerConnectingToPrinter", 513), ("diskStorageNone", 600), ("videoNone", 1000), ("audioNone", 1100), ("coprocessorNone", 1200), ("keyboardNone", 1300), ("modemNone", 1400), ("parallelPortNone", 1500), ("pointingNone", 1600), ("serialPortNone", 1700), ("tapeNone", 1800), ("clockNone", 1900), ("volatileMemoryNone", 2000), ("nonVolatileMemoryNone", 2100), ("hostSystemNone", 10100), ("scannerNone", 10200), ("copierNone", 10300), ("faxNone", 10400), ("mailboxNone", 10500), ("markerNone", 11100), ("finisherBFMNone", 11200), ("finisherMFFNone", 11300), ("finisherXIMNone", 11400), ("finisher3rdPartyNone", 11500), ("paymentInterfaceNone", 11600), ("interposerNone", 11700), ("cruNone", 20000), ("cruOther", 20001), ("cruUnknown", 20002), ("cruReady", 20003), ("cruReorder", 20004), ("cruReplace", 20005), ("cruFault", 20006), ("reserved", 40000))

class ScmHrDevInfoConditions(TextualConvention, Integer32):
    reference = "See: 'hrDeviceStatus' in the basic Device Group of the IETF Host Resources MIB (RFC 2790). See: 'scmHrDevInfoXStatus' and 'scmHrDevInfoXConditions' in the Host Resources Extensions MIB."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmHrDevInfoXConditions(TextualConvention, Integer32):
    reference = "See: 'hrDeviceStatus' in the basic Device Group of the IETF Host Resources MIB (RFC 2790). See: 'scmHrDevInfoXStatus' and 'scmHrDevInfoConditions' in the Host Resources Extensions MIB."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmHrDevMgmtCommandRequest(TextualConvention, Integer32):
    reference = "See: 'dot5Commands' in IEEE 802.5 Token Ring MIB (RFC 1748) and 'hrDeviceStatus' in IETF Host Resources MIB (RFC 2790). Compare: 'ifOperStatus' (current) and 'ifAdminStatus' (desired) in the Interfaces Group of IETF MIB-II (RFC 1213); 'RowStatus' textual convention in IETF SMIv2 (RFC 1902/2578). See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE 1387.4 / Draft 8, October 1994). See: OBJECT clause in MODULE-COMPLIANCE macro of SCMI Ext to Host Resources MIB, for compliance info. See: Section 3.4 'SCMI Standard Tagged Management Data' and Section 3.5 'Simple Device Management Requests' in SCMI Ext to Host Resources TC. See: Section 3.5.3 'Secure Simple Device Mgmt Requests' in SCMI Security TC."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 2301, 2302, 2321, 2322, 2323, 2324, 2325, 2326, 2331, 2332, 2333, 2334, 2335, 2336, 2341, 2342, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 2901, 2902, 2921, 2922, 2923, 2924, 2925, 2926, 2931, 2932, 2933, 2934, 2935, 2936, 2941, 2942))
    namedValues = NamedValues(("none", 1), ("startup", 2), ("resetWarning", 3), ("test", 4), ("shutdown", 5), ("quiesce", 6), ("resetCounters", 7), ("resetWarm", 8), ("resetCold", 9), ("resetFactory", 10), ("flushInput", 11), ("flushOutput", 12), ("flushInOut", 13), ("manage", 14), ("refresh", 15), ("warmUp", 16), ("coolDown", 17), ("energySave", 18), ("wakeUp", 19), ("powerToReady", 20), ("powerToStandby", 21), ("powerToSleep", 22), ("deviceCreate", 1301), ("deviceDelete", 1302), ("deviceList", 1303), ("deviceSet", 1304), ("deviceClean", 1305), ("deviceDisable", 1306), ("deviceEnable", 1307), ("devicePause", 1308), ("deviceResume", 1309), ("deviceShutdown", 1310), ("deviceQueueList", 1311), ("deviceJobCreate", 1312), ("deviceManage", 2301), ("deviceRestart", 2302), ("deviceInstall", 2321), ("deviceUpgrade", 2322), ("deviceBackup", 2323), ("deviceRestore", 2324), ("deviceConfigure", 2325), ("deviceDiagnose", 2326), ("deviceResetCounters", 2331), ("deviceResetWarm", 2332), ("deviceResetCold", 2333), ("deviceResetFactory", 2334), ("deviceFormat", 2335), ("deviceRefresh", 2336), ("deviceLogin", 2341), ("deviceLogout", 2342), ("entityCreate", 1901), ("entityDelete", 1902), ("entityList", 1903), ("entitySet", 1904), ("entityClean", 1905), ("entityDisable", 1906), ("entityEnable", 1907), ("entityPause", 1908), ("entityResume", 1909), ("entityShutdown", 1910), ("entityQueueList", 1911), ("entityJobCreate", 1912), ("entityManage", 2901), ("entityRestart", 2902), ("entityInstall", 2921), ("entityUpgrade", 2922), ("entityBackup", 2923), ("entityRestore", 2924), ("entityConfigure", 2925), ("entityDiagnose", 2926), ("entityResetCounters", 2931), ("entityResetWarm", 2932), ("entityResetCold", 2933), ("entityResetFactory", 2934), ("entityFormat", 2935), ("entityRefresh", 2936), ("entityLogin", 2941), ("entityLogout", 2942))

class ScmHrDevMgmtCommandData(TextualConvention, OctetString):
    reference = "See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE 1387.4 / Draft 8, October 1994). See: 'hrDeviceStatus' in the Device group of the IETF Host Resources MIB (RFC 2790). See: Section 3.4 'SCMI Standard Tagged Management Data' and Section 3.5 'Simple Device Management Requests' in SCMI Ext to Host Resources TC. See: Section 3.5.3 'Secure Simple Device Mgmt Requests' in SCMI Security TC."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ScmHrDevMgmtCommandDataTag(TextualConvention, OctetString):
    reference = "See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE 1387.4 / Draft 8, October 1994). See: 'hrDeviceStatus' in the Device group of the IETF Host Resources MIB (RFC 2790). See: Section 3.4 'SCMI Standard Tagged Management Data' and Section 3.5 'Simple Device Management Requests' in SCMI Ext to Host Resources TC. See: Section 3.5.3 'Secure Simple Device Mgmt Requests' in SCMI Security TC."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class ScmHrDevPowerModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("readyMode", 3), ("standbyMode", 4), ("sleepMode", 5), ("offMode", 6))

class ScmHrDevPowerTimeUnit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("microsecond", 3), ("millisecond", 4), ("second", 5), ("kilosecond", 6), ("megasecond", 7), ("minute", 8), ("hour", 9), ("day", 10), ("week", 11), ("month", 12), ("year", 13))

class ScmHrDevTrafficUnit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("binaryBit", 11), ("binaryNibble", 12), ("binaryOctet", 13), ("binaryLine", 14), ("textCharacter", 15), ("textWord", 16), ("textLine", 17), ("textSentence", 18), ("textParagraph", 19), ("mediaBlock", 20), ("mediaSector", 21), ("mediaRow", 22), ("mediaColumn", 23), ("mediaPacket", 24), ("mediaCell", 25), ("mediaImage", 26), ("mediaImpression", 27), ("mediaSheet", 28), ("lengthInch", 29), ("lengthFoot", 30), ("lengthYard", 31), ("lengthMile", 32), ("lengthMicrometer", 33), ("lengthMillimeter", 34), ("lengthCentimeter", 35), ("lengthMeter", 36), ("lengthKilometer", 37), ("volumeMicroliter", 38), ("volumeMilliliter", 39), ("volumeLiter", 40), ("volumeKiloliter", 41), ("weightMicrogram", 42), ("weightMilligram", 43), ("weightGram", 44), ("weightKilogram", 45), ("areaSqInch", 50), ("areaSqFoot", 51), ("areaSqYard", 52), ("areaSqMile", 53), ("areaSqMicrometer", 54), ("areaSqMillimeter", 55), ("areaSqCentimeter", 56), ("areaSqMeter", 57), ("areaSqKilometer", 58), ("areaSheet", 59), ("media100Image", 60), ("media100Impression", 61), ("media100Sheet", 62), ("length100Foot", 63), ("length100Meter", 64), ("area100SqFoot", 65), ("area10SqMeter", 66), ("area100Sheet", 67))

class ScmHrGroupSupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmHrSWRunXStatus(TextualConvention, Integer32):
    reference = "See: 'hrSWRunStatus' in the basic Software Running Group of the IETF Host Resources MIB (RFC 2790)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("other", 1), ("unknown", 2))

class ScmHrStorageDetailType(TextualConvention, Integer32):
    reference = "See: 'scmHrStorageDetailUnit' for units of storage detail."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 21, 22, 23, 24, 30, 31, 32, 33, 40, 41, 42))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("storageName", 3), ("storageAlias", 4), ("storageType", 5), ("storageDescription", 6), ("storageAllocationUnits", 7), ("storageTree", 8), ("storageContext", 9), ("storageInputBuffer", 10), ("storageOutputBuffer", 11), ("storageImageBuffer", 12), ("storageMarkerBuffer", 13), ("storagePageBuffer", 14), ("storageTranslationBuffer", 15), ("storageWorkingBuffer", 16), ("storageFontCache", 20), ("storageFormCache", 21), ("storageLogoCache", 22), ("storageMacroCache", 23), ("storageStyleCache", 24), ("storageHeapMemory", 30), ("storagePrefixMemory", 31), ("storageStackMemory", 32), ("storageWorkingMemory", 33), ("storageBaseAddress", 40), ("storageWordSize", 41), ("storagePageSize", 42))

class ScmHrStorageRealization(TextualConvention, Integer32):
    reference = "See: 'ScmHrDevInfoRealization' textual convention in the SCMI Ext to Host Resources TC. See: 'scmHrDevInfoRealization' in the Device Info group of the SCMI Ext to Host Resources MIB."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 10, 11, 12, 20, 21, 22))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("physicalSystem", 10), ("physicalProgram", 11), ("physicalThread", 12), ("logicalSystem", 20), ("logicalProgram", 21), ("logicalThread", 22))

class ScmHrDpaAvailability(TextualConvention, Integer32):
    reference = "See: Section 9.1.6.6 '[Generic attribute] Availability' and Annex A 'id-val-availability-...' in DPA (ISO/IEC 10175-1 Final Text, March 1996)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 6))
    namedValues = NamedValues(("high", 1), ("normal", 2), ("low", 3), ("none", 5), ("unknown", 6))

class ScmHrDpaConditions(TextualConvention, Integer32):
    reference = "See: Section 9.5.4 'Server-state', section 9.1.6.4 '[Generic attribute] State', and Annex A 'id-val-state-...' in DPA (ISO/IEC 10175-1 Final Text, March 1996). See: Section D.2.3 'Server State Transitions' in DPA Mgmt Service (ISO 10175-3 Draft, October 1996). See: Section 4 'Printing Utilities - Command Line Interface' in POSIX DPA Client (IEEE 1387.4, October 1994)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmHrDpaJobValidateSupport(TextualConvention, Integer32):
    reference = "See: Section 9.5.10 'Job-validates-supported' (server), section 9.2.4.12 'Job-validate' (job), and Annex A 'id-val-job-validate-...' in DPA (ISO/IEC 10175-1 Final Text, March 1996)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmHrDpaObjectClassSupport(TextualConvention, Integer32):
    reference = "See: Section 9.5.5 'Object-classes-supported' (server), section 9.1.6.1 'Object-class' (system), Annex A 'id-oc-...' in DPA (ISO/IEC 10175-1 Final Text, March 1996)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmHrDpaState(TextualConvention, Integer32):
    reference = "See: Section 9.1.6.4 '[Generic attribute] State' and Annex A 'id-val-state-...' in DPA (ISO/IEC 10175-1 Final Text, March 1996)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("ready", 1), ("onRequest", 2), ("unavailable", 3), ("unknown", 4), ("busy", 5), ("initializing", 6), ("terminating", 7))

sCmHrDummy = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999))
sCmHrDevCalendarDayOfWeek = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 1), ScmHrDevCalendarDayOfWeek())
if mibBuilder.loadTexts: sCmHrDevCalendarDayOfWeek.setStatus('current')
sCmHrDevCalendarTimeOfDay = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 2), ScmHrDevCalendarTimeOfDay())
if mibBuilder.loadTexts: sCmHrDevCalendarTimeOfDay.setStatus('current')
sCmHrDevDetailType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 3), ScmHrDevDetailType())
if mibBuilder.loadTexts: sCmHrDevDetailType.setStatus('current')
sCmHrDevDetailUnitClass = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 4), ScmHrDevDetailUnitClass())
if mibBuilder.loadTexts: sCmHrDevDetailUnitClass.setStatus('current')
sCmHrDevInfoRealization = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 5), ScmHrDevInfoRealization())
if mibBuilder.loadTexts: sCmHrDevInfoRealization.setStatus('current')
sCmHrDevInfoStatus = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 6), ScmHrDevInfoStatus())
if mibBuilder.loadTexts: sCmHrDevInfoStatus.setStatus('current')
sCmHrDevInfoXStatus = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 7), ScmHrDevInfoXStatus())
if mibBuilder.loadTexts: sCmHrDevInfoXStatus.setStatus('current')
sCmHrDevInfoConditions = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 8), ScmHrDevInfoConditions())
if mibBuilder.loadTexts: sCmHrDevInfoConditions.setStatus('current')
sCmHrDevInfoXConditions = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 9), ScmHrDevInfoXConditions())
if mibBuilder.loadTexts: sCmHrDevInfoXConditions.setStatus('current')
sCmHrDevMgmtCommandRequest = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 10), ScmHrDevMgmtCommandRequest())
if mibBuilder.loadTexts: sCmHrDevMgmtCommandRequest.setStatus('current')
sCmHrDevMgmtCommandData = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 11), ScmHrDevMgmtCommandData())
if mibBuilder.loadTexts: sCmHrDevMgmtCommandData.setStatus('current')
sCmHrDevMgmtCommandDataTag = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 12), ScmHrDevMgmtCommandDataTag())
if mibBuilder.loadTexts: sCmHrDevMgmtCommandDataTag.setStatus('current')
sCmHrDevPowerModeType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 13), ScmHrDevPowerModeType())
if mibBuilder.loadTexts: sCmHrDevPowerModeType.setStatus('current')
sCmHrDevPowerTimeUnit = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 14), ScmHrDevPowerTimeUnit())
if mibBuilder.loadTexts: sCmHrDevPowerTimeUnit.setStatus('current')
sCmHrDevTrafficUnit = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 15), ScmHrDevTrafficUnit())
if mibBuilder.loadTexts: sCmHrDevTrafficUnit.setStatus('current')
sCmHrGroupSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 16), ScmHrGroupSupport())
if mibBuilder.loadTexts: sCmHrGroupSupport.setStatus('current')
sCmHrSWRunXStatus = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 17), ScmHrSWRunXStatus())
if mibBuilder.loadTexts: sCmHrSWRunXStatus.setStatus('current')
sCmHrStorageDetailType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 18), ScmHrStorageDetailType())
if mibBuilder.loadTexts: sCmHrStorageDetailType.setStatus('current')
sCmHrStorageRealization = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 19), ScmHrStorageRealization())
if mibBuilder.loadTexts: sCmHrStorageRealization.setStatus('current')
sCmHrDpaAvailability = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 20), ScmHrDpaAvailability())
if mibBuilder.loadTexts: sCmHrDpaAvailability.setStatus('current')
sCmHrDpaConditions = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 21), ScmHrDpaConditions())
if mibBuilder.loadTexts: sCmHrDpaConditions.setStatus('current')
sCmHrDpaJobValidateSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 22), ScmHrDpaJobValidateSupport())
if mibBuilder.loadTexts: sCmHrDpaJobValidateSupport.setStatus('current')
sCmHrDpaObjectClassSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 23), ScmHrDpaObjectClassSupport())
if mibBuilder.loadTexts: sCmHrDpaObjectClassSupport.setStatus('current')
sCmHrDpaState = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 24), ScmHrDpaState())
if mibBuilder.loadTexts: sCmHrDpaState.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-HOST-RESOURCES-EXT-TC", scmHrDeviceFax=scmHrDeviceFax, scmHrAdminDeviceService=scmHrAdminDeviceService, scmHrDeviceFlashDIMMFileStore=scmHrDeviceFlashDIMMFileStore, sCmHrGroupSupport=sCmHrGroupSupport, scmHrDeviceInterposer=scmHrDeviceInterposer, ScmHrDevInfoRealization=ScmHrDevInfoRealization, ScmHrDevCalendarTimeOfDay=ScmHrDevCalendarTimeOfDay, scmHrAdminDeviceRefresh=scmHrAdminDeviceRefresh, ScmHrDevPowerTimeUnit=ScmHrDevPowerTimeUnit, scmHrAdminCommsService=scmHrAdminCommsService, scmHrAdminDevicePowerToSleep=scmHrAdminDevicePowerToSleep, sCmHrDevInfoConditions=sCmHrDevInfoConditions, scmHrCruTransferRollerModule=scmHrCruTransferRollerModule, sCmHrDevDetailUnitClass=sCmHrDevDetailUnitClass, scmHrAdminDeviceFlushInOut=scmHrAdminDeviceFlushInOut, scmHrCruFuserWebModule=scmHrCruFuserWebModule, scmHrAdminDeviceCoolDown=scmHrAdminDeviceCoolDown, scmHrAdminDeviceResetWarning=scmHrAdminDeviceResetWarning, sCmHrDevInfoStatus=sCmHrDevInfoStatus, ScmHrStorageRealization=ScmHrStorageRealization, scmHrCruCleanerUnitModule=scmHrCruCleanerUnitModule, sCmHrDevCalendarDayOfWeek=sCmHrDevCalendarDayOfWeek, scmHrCruFilterModule=scmHrCruFilterModule, scmHrAdminDeviceManage=scmHrAdminDeviceManage, scmHrDeviceTypes=scmHrDeviceTypes, ScmHrDevPowerModeType=ScmHrDevPowerModeType, sCmHrDummy=sCmHrDummy, scmHrAdminDeviceOperationTypes=scmHrAdminDeviceOperationTypes, scmHrAdminDeviceTest=scmHrAdminDeviceTest, scmHrAdminDeviceWarmUp=scmHrAdminDeviceWarmUp, scmHrDeviceFinisher=scmHrDeviceFinisher, scmHrDeviceMailboxSorter=scmHrDeviceMailboxSorter, sCmHrDpaAvailability=sCmHrDpaAvailability, scmHrCruAdfFeedHeadModule=scmHrCruAdfFeedHeadModule, scmHrCruTonerBottleModule=scmHrCruTonerBottleModule, scmHrAdminDeviceNone=scmHrAdminDeviceNone, scmHrDeviceFinisher3rdParty=scmHrDeviceFinisher3rdParty, scmHrDeviceScannerHistory=scmHrDeviceScannerHistory, scmHrAdminDeviceWakeUp=scmHrAdminDeviceWakeUp, ScmHrDpaConditions=ScmHrDpaConditions, scmHrAdminDeviceFlushInput=scmHrAdminDeviceFlushInput, scmHrDeviceFinisherXIM=scmHrDeviceFinisherXIM, scmHrDeviceUSBPort=scmHrDeviceUSBPort, ScmHrDevCalendarDayOfWeek=ScmHrDevCalendarDayOfWeek, scmHrAdminDeviceFlushOutput=scmHrAdminDeviceFlushOutput, sCmHrDpaConditions=sCmHrDpaConditions, scmHrDevicePaymentInterface=scmHrDevicePaymentInterface, sCmHrDpaState=sCmHrDpaState, scmHrAdminDeviceResetFactory=scmHrAdminDeviceResetFactory, scmHrCruPFPFeedRollModule=scmHrCruPFPFeedRollModule, scmHrDeviceSorter=scmHrDeviceSorter, scmHrDeviceHostSystemHistory=scmHrDeviceHostSystemHistory, ScmHrDpaObjectClassSupport=ScmHrDpaObjectClassSupport, sCmHrDevInfoRealization=sCmHrDevInfoRealization, scmHrCruPFPRetardRollModule=scmHrCruPFPRetardRollModule, scmHrDeviceFinisherBFM=scmHrDeviceFinisherBFM, scmHrAdminDevicePowerToReady=scmHrAdminDevicePowerToReady, sCmHrDevTrafficUnit=sCmHrDevTrafficUnit, ScmHrDevInfoConditions=ScmHrDevInfoConditions, ScmHrDpaAvailability=ScmHrDpaAvailability, scmHrAdminObjectService=scmHrAdminObjectService, scmHrCruCollectorBottleModule=scmHrCruCollectorBottleModule, scmHrAdminDocService=scmHrAdminDocService, sCmHrStorageRealization=sCmHrStorageRealization, sCmHrDevPowerTimeUnit=sCmHrDevPowerTimeUnit, sCmHrDevInfoXConditions=sCmHrDevInfoXConditions, sCmHrDevMgmtCommandDataTag=sCmHrDevMgmtCommandDataTag, ScmHrSWRunXStatus=ScmHrSWRunXStatus, ScmHrDevMgmtCommandDataTag=ScmHrDevMgmtCommandDataTag, scmHrAdminDeviceResetCold=scmHrAdminDeviceResetCold, ScmHrStorageDetailType=ScmHrStorageDetailType, ScmHrGroupSupport=ScmHrGroupSupport, scmHrAdminDeviceResetWarm=scmHrAdminDeviceResetWarm, scmHrAdminJobService=scmHrAdminJobService, scmHrCruTransferUnitModule=scmHrCruTransferUnitModule, scmHrDeviceFaxHistory=scmHrDeviceFaxHistory, scmHrCruTrayFeedHeadModule=scmHrCruTrayFeedHeadModule, scmHrCruFuserModule=scmHrCruFuserModule, sCmHrDevDetailType=sCmHrDevDetailType, scmHrDevicePrintAppliance=scmHrDevicePrintAppliance, ScmHrDevInfoStatus=ScmHrDevInfoStatus, scmHrAdminDevicePowerToStandby=scmHrAdminDevicePowerToStandby, ScmHrDevTrafficUnit=ScmHrDevTrafficUnit, sCmHrDevInfoXStatus=sCmHrDevInfoXStatus, scmHrAdminDeviceStartup=scmHrAdminDeviceStartup, sCmHrDevCalendarTimeOfDay=sCmHrDevCalendarTimeOfDay, scmHrTC=scmHrTC, scmHrCruXerographicModule=scmHrCruXerographicModule, scmHrDeviceFlashDIMMBootLoader=scmHrDeviceFlashDIMMBootLoader, scmHrAdminSecurityService=scmHrAdminSecurityService, scmHrAdminDeviceEnergySave=scmHrAdminDeviceEnergySave, ScmHrDevInfoXConditions=ScmHrDevInfoXConditions, sCmHrSWRunXStatus=sCmHrSWRunXStatus, scmHrDeviceMarker=scmHrDeviceMarker, ScmHrDevMgmtCommandData=ScmHrDevMgmtCommandData, sCmHrStorageDetailType=sCmHrStorageDetailType, scmHrDeviceCopier=scmHrDeviceCopier, scmHrDeviceFeeder=scmHrDeviceFeeder, scmHrAdminServiceTypes=scmHrAdminServiceTypes, scmHrDeviceScanner=scmHrDeviceScanner, scmHrDevicePrinterHistory=scmHrDevicePrinterHistory, scmHrAdminDeviceQuiesce=scmHrAdminDeviceQuiesce, scmHrAdminDeviceResetCounters=scmHrAdminDeviceResetCounters, sCmHrDevMgmtCommandData=sCmHrDevMgmtCommandData, sCmHrDpaObjectClassSupport=sCmHrDpaObjectClassSupport, ScmHrDpaJobValidateSupport=ScmHrDpaJobValidateSupport, ScmHrDevDetailType=ScmHrDevDetailType, sCmHrDevMgmtCommandRequest=sCmHrDevMgmtCommandRequest, scmHrAdminDeviceShutdown=scmHrAdminDeviceShutdown, ScmHrDevDetailUnitClass=ScmHrDevDetailUnitClass, ScmHrDpaState=ScmHrDpaState, ScmHrDevMgmtCommandRequest=ScmHrDevMgmtCommandRequest, sCmHrDpaJobValidateSupport=sCmHrDpaJobValidateSupport, sCmHrDevPowerModeType=sCmHrDevPowerModeType, scmHrAdminServerService=scmHrAdminServerService, PYSNMP_MODULE_ID=scmHrTC, scmHrDeviceMailbox=scmHrDeviceMailbox, scmHrDeviceCopierHistory=scmHrDeviceCopierHistory, scmHrDeviceFinisherMFF=scmHrDeviceFinisherMFF, ScmHrDevInfoXStatus=ScmHrDevInfoXStatus, scmHrDeviceHostSystem=scmHrDeviceHostSystem)
