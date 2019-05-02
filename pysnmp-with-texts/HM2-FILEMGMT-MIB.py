#
# PySNMP MIB module HM2-FILEMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-FILEMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:31:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
HmTimeSeconds1970, hm2ConfigurationMibs, HmEnabledStatus = mibBuilder.importSymbols("HM2-TC-MIB", "HmTimeSeconds1970", "hm2ConfigurationMibs", "HmEnabledStatus")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, ObjectIdentity, Counter64, Bits, IpAddress, Integer32, iso, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "ObjectIdentity", "Counter64", "Bits", "IpAddress", "Integer32", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
hm2FileMgmtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21))
hm2FileMgmtMib.setRevisions(('2011-03-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2FileMgmtMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2FileMgmtMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2FileMgmtMib.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2FileMgmtMib.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2FileMgmtMib.setDescription('Hirschmann File Management MIB. Copyright (C) 2011. All Rights Reserved.')
hm2FileMgmtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 0))
hm2FileMgmtMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1))
hm2FileMgmtSNMPExtensionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 3))
hm2FileMgmtProfileGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1))
hm2FileMgmtActionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2))
hm2FileMgmtStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3))
hm2FileMgmtConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4))
hm2FMActionTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1), )
if mibBuilder.loadTexts: hm2FMActionTable.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionTable.setDescription('A list of profiles stored in NV memory.')
hm2FMActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1), ).setIndexNames((0, "HM2-FILEMGMT-MIB", "hm2FMActionType"), (0, "HM2-FILEMGMT-MIB", "hm2FMActionItemType"), (0, "HM2-FILEMGMT-MIB", "hm2FMActionSourceType"), (0, "HM2-FILEMGMT-MIB", "hm2FMActionDestinationType"))
if mibBuilder.loadTexts: hm2FMActionEntry.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionEntry.setDescription('A profile entry.')
hm2FMActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nop", 1), ("copy", 2), ("clear", 3), ("swap", 4))))
if mibBuilder.loadTexts: hm2FMActionType.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionType.setDescription('Type of the action to be performed.')
hm2FMActionItemType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 10, 15, 20, 30, 31, 40, 41, 42, 50, 51, 52, 53, 60, 65, 70, 71, 80, 81, 82, 83, 84, 90, 100))).clone(namedValues=NamedValues(("none", 1), ("config", 10), ("filesystem", 15), ("script", 20), ("firmware", 30), ("bootcode", 31), ("eventlog", 40), ("audittrail", 41), ("traplog", 42), ("sysinfo", 50), ("sfpWhiteList", 51), ("cliBanner", 52), ("sysinfoall", 53), ("sshkey", 60), ("httpsServerCert", 65), ("tcpdumpcap", 70), ("tcpdumpfilter", 71), ("camcert", 80), ("ldapCacert", 81), ("mailCacert", 82), ("syslogCacert", 83), ("camcertPEM", 84), ("edsFile", 90), ("gsdmlFile", 100))))
if mibBuilder.loadTexts: hm2FMActionItemType.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionItemType.setDescription('Type of the item to be processed.')
hm2FMActionSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 6, 7, 10, 11, 20))).clone(namedValues=NamedValues(("none", 1), ("nvm", 2), ("envm", 3), ("buffered", 6), ("persistent", 7), ("runningConfig", 10), ("system", 11), ("server", 20))))
if mibBuilder.loadTexts: hm2FMActionSourceType.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionSourceType.setDescription('Type of the source object to be processed.')
hm2FMActionDestinationType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 10, 11, 20))).clone(namedValues=NamedValues(("none", 1), ("nvm", 2), ("envm", 3), ("runningConfig", 10), ("system", 11), ("server", 20))))
if mibBuilder.loadTexts: hm2FMActionDestinationType.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionDestinationType.setDescription('Type of the destination object to be processed.')
hm2FMActionActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMActionActivate.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionActivate.setDescription('In case of a set operation: If the value to be written matches with the result of hm2FMActionActivateKey, the action is started. In case of a read operation, it will always reflect the key of the last successful operation.')
hm2FMActionSourceData = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMActionSourceData.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionSourceData.setDescription('Additional data for the source object. This could, for example, be a profile name or URL')
hm2FMActionDestinationData = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMActionDestinationData.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionDestinationData.setDescription('Additional data for the source object. This could be for example a profile name or URL')
hm2FMActionActivateResult = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("paramError", 2), ("busy", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMActionActivateResult.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionActivateResult.setDescription('Either returns ok(1) if the action is successfully started, param-error(2) if there is some problem with the given parameters or busy(3) if there is still an action in progress.')
hm2FMActionActivateResultText = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMActionActivateResultText.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionActivateResultText.setDescription('Text describing why the start of the operation has failed.')
hm2FMActionStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("running", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMActionStatus.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionStatus.setDescription('Returns the running status of the action.')
hm2FMActionPercentReady = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMActionPercentReady.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionPercentReady.setDescription('Estimation of how many percent of the operation is done.')
hm2FMActionResult = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMActionResult.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionResult.setDescription('Error status of the last action which has been performed.')
hm2FMActionResultText = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMActionResultText.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionResultText.setDescription('Either OK or a descriptive text giving a reason why the last operation failed')
hm2FMActionActivateKey = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMActionActivateKey.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionActivateKey.setDescription('An advisory lock used to ensure that different management entities can not interfere with each others actions. The value read from this variable must be used to start the action by applying to the object hm2FMActionActivate. ')
hm2FMActionContainerPassword = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMActionContainerPassword.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionContainerPassword.setDescription('.')
hm2FMActionParameter = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("all", 2))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMActionParameter.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionParameter.setDescription('This variable defines what acion to be done based on the value. By default it has value as none.')
hm2FMActionSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 21), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMActionSourceInterface.setStatus('current')
if mibBuilder.loadTexts: hm2FMActionSourceInterface.setDescription('This variable defines the interface from which the source IP address will be taken for the file transfer session. The frames will not necessarily be sent on this interface, only the IP address of the interface will be used as source. By default it has value 0.')
hm2FMProfileTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1), )
if mibBuilder.loadTexts: hm2FMProfileTable.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileTable.setDescription('A list of profiles stored in NV memory.')
hm2FMProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1), ).setIndexNames((0, "HM2-FILEMGMT-MIB", "hm2FMProfileStorageType"), (0, "HM2-FILEMGMT-MIB", "hm2FMProfileIndex"))
if mibBuilder.loadTexts: hm2FMProfileEntry.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileEntry.setDescription('A profile entry.')
hm2FMProfileStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nvm", 1), ("envm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileStorageType.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileStorageType.setDescription('Type of storage of the profile entry.')
hm2FMProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileIndex.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileIndex.setDescription('Index of the profile entry.')
hm2FMProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileName.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileName.setDescription('Name of the entry consisting of alphanumeric characters plus hyphen and underscore.')
hm2FMProfileDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 4), HmTimeSeconds1970()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileDateTime.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileDateTime.setDescription('Time and date of last write access using the content of the variable hm2SystemTime.')
hm2FMProfileActive = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMProfileActive.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileActive.setDescription('Setting the variable to active(1) enables the profile so that it will be used the next time the configuration is reloaded. Setting the value to inactive(2) is not allowed since there must be always at least one profile with the state set to active(1).')
hm2FMProfileAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMProfileAction.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileAction.setDescription('Action to be performed on the profile entry. Setting the value to delete(2) erases the profile. It is not possible to delete the currently active profile.')
hm2FMProfileDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileDeviceType.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileDeviceType.setDescription('Manufacturer-defined product identifier (product family + product ID). Example: Object-ID 1.3.6.1.4.1.248.11.2.1.1 is the hm2ProductFamily EES and Object-ID 1.3.6.1.4.1.248.11.2.1.1.2 is the Product ID for ees25-0600')
hm2FMProfileEncryptionActive = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileEncryptionActive.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileEncryptionActive.setDescription('The profile is encrypted if this variable is set to active(true). It is not encrypted in case of inactive(false).')
hm2FMProfileEncryptionVerified = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileEncryptionVerified.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileEncryptionVerified.setDescription('This variable indicates true if an encrypted profile can be successfully decrypted by the device. In case of an encryption password mismatch, the verification fails the value is false. If the corresponding profile is not encrypted, this variable is set to true.')
hm2FMProfileSwMajorRelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileSwMajorRelNum.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileSwMajorRelNum.setDescription('Shows the major release number of the firmware, the profile was created on.')
hm2FMProfileSwMinorRelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileSwMinorRelNum.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileSwMinorRelNum.setDescription('Shows the minor release number of the firmware, the profile was created on.')
hm2FMProfileSwBugfixRelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileSwBugfixRelNum.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileSwBugfixRelNum.setDescription('Shows the bugfix release number of the firmware, the profile was created on.')
hm2FMProfileFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(40, 40)).setFixedLength(40)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileFingerprint.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileFingerprint.setDescription('HEX String representation of profile content fingerprint. Consists of characters (0..9A..F) to represent a hexadecimal number. It will contain the string invalid, if the corresponding file does not contain a correct formatted SHA1 hash as fingerprint.')
hm2FMProfileFingerprintVerified = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMProfileFingerprintVerified.setStatus('current')
if mibBuilder.loadTexts: hm2FMProfileFingerprintVerified.setDescription("This variable indicates true if the configuration profiles fingerprint matches the profile's configuration data. In case of a fingerprint, the variable is set to false.")
hm2FMNvmState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("outOfSync", 2), ("busy", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMNvmState.setStatus('current')
if mibBuilder.loadTexts: hm2FMNvmState.setDescription('This variable returns ok(1) if the contents of the currently used configuration is the same as that stored in NV memory or outOfsync(2) if there are any differences. The variable returns busy(3) if the process to determine a possible state change is currently running.')
hm2FMEnvmState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("outOfSync", 2), ("absent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMEnvmState.setStatus('current')
if mibBuilder.loadTexts: hm2FMEnvmState.setDescription('This variable returns ok(1) if the contents of the currently used configuration on the active external non-volatile memory is the same than that stored in NV memory, outOfsync(2) if there are any differences. If the value is absent(3), then the external memory device is not connected.')
hm2FMBootParamState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("outOfSync", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FMBootParamState.setStatus('current')
if mibBuilder.loadTexts: hm2FMBootParamState.setDescription('Returns outOfSync(2) if the boot parameters that were applied during startup are not in sync with the currently stored boot parameters, otherwise ok(1).')
hm2FileMgmtConfigWatchdogControl = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1))
hm2ConfigWatchdogAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2ConfigWatchdogAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigWatchdogAdminStatus.setDescription('Administrative status of the configuration watchdog. enable(1): start/trigger the watchdog timer disable(2): turn off the watchdog This feature provides recovery from situations where the device cannot be reached by the management station anymore. Whenever this variable is set to enable(1), the value of hm2ConfigWatchdogTimeInterval is loaded into the watchdog timer. This timer must be triggered before hm2ConfigWatchdogTimerValue reaches 0. If the watchdog timer expires, the last saved configuration of the device will be reapplied. The watchdog is triggered by MIB read and write accesses.')
hm2ConfigWatchdogOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 2), HmEnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2ConfigWatchdogOperStatus.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigWatchdogOperStatus.setDescription('Operational status of the configuration watchdog. enable(1): watchdog up and running disable(2): watchdog inactive')
hm2ConfigWatchdogTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 600)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2ConfigWatchdogTimeInterval.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigWatchdogTimeInterval.setDescription('Period of the watchdog timer in seconds.')
hm2ConfigWatchdogTimerValue = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2ConfigWatchdogTimerValue.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigWatchdogTimerValue.setDescription('Current countdown value of the watchdog timer in seconds.')
hm2ConfigWatchdogIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2ConfigWatchdogIPAddressType.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigWatchdogIPAddressType.setDescription('IP address type of station that triggers the watchdog.')
hm2ConfigWatchdogIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2ConfigWatchdogIPAddress.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigWatchdogIPAddress.setDescription('IP address of station that currently triggers the watchdog.')
hm2FileMgmtServerAccessGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 2))
hm2FMServerUserName = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMServerUserName.setStatus('current')
if mibBuilder.loadTexts: hm2FMServerUserName.setDescription('Login name for the used file transport protocol.')
hm2FMServerPassword = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FMServerPassword.setStatus('current')
if mibBuilder.loadTexts: hm2FMServerPassword.setDescription('Password for the used file transport protocol.')
hm2FileMgmtSecurityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 4))
hm2FileMgmtConfigPasswordStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 4, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FileMgmtConfigPasswordStatus.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtConfigPasswordStatus.setDescription("Returns 'true' if a configuration password is set, otherwise 'false'.")
hm2FileMgmtConfigPasswordChange = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FileMgmtConfigPasswordChange.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtConfigPasswordChange.setDescription("Password to encrypt confidential information in the configuration file. Format: '[old password]|[new password]' set password: '|[new password]' change password: '[old password]|[new password]' remove password: '[old password]|' Valid password characters are any DisplayString characters except '|'. When this object is read, the zero-length (empty) string is returned. Setting the zero-length string has no effect.")
hm2FileMgmtGlobalSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 9), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FileMgmtGlobalSourceInterface.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtGlobalSourceInterface.setDescription('This variable defines the global source-interface used by file-transfers in case hm2FMActionSourceInterface is not configured by the user. The frames will not necessarily be sent on this interface, only the IP address of the interface will be used as source. By default it has value 0.')
hm2FileMgmtConfigCompatibilityMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("hiosV1V2", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FileMgmtConfigCompatibilityMode.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtConfigCompatibilityMode.setDescription("Set 'hiosV1V2' only if a configuration file needs to be migrated to a device running HiOS 01.x.xx / 02.x.xx software. Otherwise for normal operation it is recommended to set the compatibility mode to the default 'disable'.")
hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 1))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn.setDescription('Indicates a configuration profile was activated succesfully, but several config items failed to initialize.')
hm2FileMgmtSESCfgActivateErrorReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 2))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgActivateErrorReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgActivateErrorReturn.setDescription('Indicates a configuration profile could not be activated.')
hm2FileMgmtSESCfgActivateIncomlpeteReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 3))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgActivateIncomlpeteReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgActivateIncomlpeteReturn.setDescription('Indicates an incomlete activation of a configuration profile.')
hm2FileMgmtSESCfgMgrCopyCommandErrorReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 4))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrCopyCommandErrorReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrCopyCommandErrorReturn.setDescription("Indicates a failure of a COPY command given to the Config-Manager's command engine.")
hm2FileMgmtSESCfgMgrClearCommandErrorReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 5))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrClearCommandErrorReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrClearCommandErrorReturn.setDescription("Indicates a failure of a CLEAR command given to the Config-Manager's command engine.")
hm2FileMgmtSESCfgMgrSwapCommandErrorReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 6))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrSwapCommandErrorReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrSwapCommandErrorReturn.setDescription("Indicates a failure of a SWAP command given to the Config-Manager's command engine.")
hm2FileMgmtSESCfgErrorReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 7))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgErrorReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgErrorReturn.setDescription('Indicates a CFG test error.')
hm2FileMgmtSESCfgMgrCommandActivateErrorReturn = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 8))
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrCommandActivateErrorReturn.setStatus('current')
if mibBuilder.loadTexts: hm2FileMgmtSESCfgMgrCommandActivateErrorReturn.setDescription('Indicates a failure because other Config-Manager command is running.')
hm2ConfigurationSavedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 21, 0, 1)).setObjects(("HM2-FILEMGMT-MIB", "hm2FMNvmState"), ("HM2-FILEMGMT-MIB", "hm2FMEnvmState"))
if mibBuilder.loadTexts: hm2ConfigurationSavedTrap.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigurationSavedTrap.setDescription('This trap is sent after the configuration of the agent was successfully saved.')
hm2ConfigurationChangedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 21, 0, 2)).setObjects(("HM2-FILEMGMT-MIB", "hm2FMNvmState"))
if mibBuilder.loadTexts: hm2ConfigurationChangedTrap.setStatus('current')
if mibBuilder.loadTexts: hm2ConfigurationChangedTrap.setDescription('This trap is sent if there is a change in the synchronization status between currently running and the saved configuration so that the value of hm2FMNvmState changes.')
mibBuilder.exportSymbols("HM2-FILEMGMT-MIB", hm2FMProfileTable=hm2FMProfileTable, hm2FMBootParamState=hm2FMBootParamState, hm2FileMgmtSESCfgMgrSwapCommandErrorReturn=hm2FileMgmtSESCfgMgrSwapCommandErrorReturn, hm2FMActionPercentReady=hm2FMActionPercentReady, hm2FileMgmtGlobalSourceInterface=hm2FileMgmtGlobalSourceInterface, hm2FMActionEntry=hm2FMActionEntry, hm2FMActionDestinationType=hm2FMActionDestinationType, hm2FileMgmtSESCfgErrorReturn=hm2FileMgmtSESCfgErrorReturn, PYSNMP_MODULE_ID=hm2FileMgmtMib, hm2FMActionActivateResultText=hm2FMActionActivateResultText, hm2FMActionParameter=hm2FMActionParameter, hm2FileMgmtConfigPasswordChange=hm2FileMgmtConfigPasswordChange, hm2ConfigWatchdogIPAddressType=hm2ConfigWatchdogIPAddressType, hm2FMProfileSwMinorRelNum=hm2FMProfileSwMinorRelNum, hm2ConfigWatchdogTimeInterval=hm2ConfigWatchdogTimeInterval, hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn=hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn, hm2FMActionDestinationData=hm2FMActionDestinationData, hm2FMProfileEncryptionVerified=hm2FMProfileEncryptionVerified, hm2ConfigWatchdogAdminStatus=hm2ConfigWatchdogAdminStatus, hm2ConfigWatchdogIPAddress=hm2ConfigWatchdogIPAddress, hm2FileMgmtActionGroup=hm2FileMgmtActionGroup, hm2ConfigurationChangedTrap=hm2ConfigurationChangedTrap, hm2FMActionResult=hm2FMActionResult, hm2FMProfileAction=hm2FMProfileAction, hm2FileMgmtSNMPExtensionGroup=hm2FileMgmtSNMPExtensionGroup, hm2FMActionSourceInterface=hm2FMActionSourceInterface, hm2FMActionContainerPassword=hm2FMActionContainerPassword, hm2FMNvmState=hm2FMNvmState, hm2FMActionActivate=hm2FMActionActivate, hm2FMActionStatus=hm2FMActionStatus, hm2FMProfileStorageType=hm2FMProfileStorageType, hm2ConfigWatchdogOperStatus=hm2ConfigWatchdogOperStatus, hm2FileMgmtSESCfgActivateIncomlpeteReturn=hm2FileMgmtSESCfgActivateIncomlpeteReturn, hm2FileMgmtConfigGroup=hm2FileMgmtConfigGroup, hm2FMProfileDeviceType=hm2FMProfileDeviceType, hm2FileMgmtSESCfgMgrCopyCommandErrorReturn=hm2FileMgmtSESCfgMgrCopyCommandErrorReturn, hm2FMProfileSwBugfixRelNum=hm2FMProfileSwBugfixRelNum, hm2FMProfileFingerprint=hm2FMProfileFingerprint, hm2FileMgmtStatusGroup=hm2FileMgmtStatusGroup, hm2FMProfileIndex=hm2FMProfileIndex, hm2FileMgmtSESCfgMgrClearCommandErrorReturn=hm2FileMgmtSESCfgMgrClearCommandErrorReturn, hm2FMProfileEntry=hm2FMProfileEntry, hm2FileMgmtServerAccessGroup=hm2FileMgmtServerAccessGroup, hm2ConfigWatchdogTimerValue=hm2ConfigWatchdogTimerValue, hm2FMActionResultText=hm2FMActionResultText, hm2FMProfileDateTime=hm2FMProfileDateTime, hm2FileMgmtNotifications=hm2FileMgmtNotifications, hm2FMEnvmState=hm2FMEnvmState, hm2FMServerPassword=hm2FMServerPassword, hm2FileMgmtProfileGroup=hm2FileMgmtProfileGroup, hm2FileMgmtConfigPasswordStatus=hm2FileMgmtConfigPasswordStatus, hm2FMProfileSwMajorRelNum=hm2FMProfileSwMajorRelNum, hm2FileMgmtSESCfgActivateErrorReturn=hm2FileMgmtSESCfgActivateErrorReturn, hm2FMActionActivateKey=hm2FMActionActivateKey, hm2FMActionItemType=hm2FMActionItemType, hm2FMServerUserName=hm2FMServerUserName, hm2FileMgmtSESCfgMgrCommandActivateErrorReturn=hm2FileMgmtSESCfgMgrCommandActivateErrorReturn, hm2FMActionTable=hm2FMActionTable, hm2FileMgmtMibObjects=hm2FileMgmtMibObjects, hm2FileMgmtConfigCompatibilityMode=hm2FileMgmtConfigCompatibilityMode, hm2FMProfileEncryptionActive=hm2FMProfileEncryptionActive, hm2FMProfileName=hm2FMProfileName, hm2FMActionActivateResult=hm2FMActionActivateResult, hm2FMActionSourceType=hm2FMActionSourceType, hm2FileMgmtSecurityGroup=hm2FileMgmtSecurityGroup, hm2FMProfileActive=hm2FMProfileActive, hm2ConfigurationSavedTrap=hm2ConfigurationSavedTrap, hm2FMActionType=hm2FMActionType, hm2FileMgmtMib=hm2FileMgmtMib, hm2FileMgmtConfigWatchdogControl=hm2FileMgmtConfigWatchdogControl, hm2FMActionSourceData=hm2FMActionSourceData, hm2FMProfileFingerprintVerified=hm2FMProfileFingerprintVerified)
