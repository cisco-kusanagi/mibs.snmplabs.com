#
# PySNMP MIB module ADVA-FSPR7-CFM-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADVA-FSPR7-CFM-EXTENSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:15:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ServiceImpairment, neEventLogTimeStamp, fspR7, TrapAlarmSeverity, neEventLogIdentityTranslation = mibBuilder.importSymbols("ADVA-MIB", "ServiceImpairment", "neEventLogTimeStamp", "fspR7", "TrapAlarmSeverity", "neEventLogIdentityTranslation")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, Counter64, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, MibIdentifier, Gauge32, iso, ObjectIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "iso", "ObjectIdentity", "Bits", "TimeTicks")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
cfmExtensionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6))
cfmExtensionMIB.setRevisions(('2011-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cfmExtensionMIB.setRevisionsDescriptions(('FSP3000 F7 Release 10.2.2 MIB.',))
if mibBuilder.loadTexts: cfmExtensionMIB.setLastUpdated('201102030000Z')
if mibBuilder.loadTexts: cfmExtensionMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: cfmExtensionMIB.setContactInfo('EMEA Support Phone : +49 89 89 0665 848 Fax : +49 89 89 0665 22848 Email : support@advaoptical.com North American Support Phone : 886 442 ADVA (2382) (toll-free within the US, Canada and Mexico) Fax : + 1 806 741 8529 (elsewhere) Email : support-usa@advaoptical.com Asia Pacific Support Phone : + 1 866 442 2382 (other toll-free numbers available in some countries) Email : support-asia@advaoptical.com')
if mibBuilder.loadTexts: cfmExtensionMIB.setDescription('This is a MIB definition for ADVA AG Optical Networking CFM extension objects.')
cfmAlarmMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1))
cfmAlarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1))
cfmAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2))
cfmAlarmsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0))
class CfmAlarmType(TextualConvention, Integer32):
    description = 'The list of supported CFM alarms.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 13000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010))
    namedValues = NamedValues(("undefined", 0), ("cfmOosDisabled", 13000), ("cfmOosManagement", 13001), ("cfmOosMaintenance", 13002), ("cfmOosAins", 13003), ("cfmPriVidNotEqualExtVid", 13004), ("cfmServerSignalFailure", 13005), ("cfmRemoteDefectIndication", 13006), ("cfmCcmMacStatus", 13007), ("cfmCcmError", 13008), ("cfmCcmLost", 13009), ("cfmCcmXConn", 13010))

mepAlarmSeverityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10), )
if mibBuilder.loadTexts: mepAlarmSeverityTable.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverityTable.setDescription('This table contains all alarms existing on Maintanance End Points.')
mepAlarmSeverityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1), ).setIndexNames((0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMdIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMaNetIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMepIdentifier"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityType"))
if mibBuilder.loadTexts: mepAlarmSeverityEntry.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverityEntry.setDescription('Every row of this table represents particular alarm.')
mepAlarmSeverityMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mepAlarmSeverityMdIndex.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverityMdIndex.setDescription('The index to the Maintenance Domain table.')
mepAlarmSeverityMaNetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 2), Unsigned32())
if mibBuilder.loadTexts: mepAlarmSeverityMaNetIndex.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverityMaNetIndex.setDescription('The index of the Maintenance Association Network table. ')
mepAlarmSeverityMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 3), Unsigned32())
if mibBuilder.loadTexts: mepAlarmSeverityMepIdentifier.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverityMepIdentifier.setDescription('The index of the Maintenance Association End Point tabke. ')
mepAlarmSeverityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 4), CfmAlarmType())
if mibBuilder.loadTexts: mepAlarmSeverityType.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverityType.setDescription('This object identifies the type of alarm.')
mepAlarmSeverityValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 5), TrapAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepAlarmSeverityValue.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverityValue.setDescription('This object identifies the severity assigned to this alarm.')
mepAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11), )
if mibBuilder.loadTexts: mepAlarmTable.setStatus('current')
if mibBuilder.loadTexts: mepAlarmTable.setDescription('This table contains all raised alarms on Maintanance End Points.')
mepAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1), ).setIndexNames((0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMdIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMaNetIndex"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMepIdentifier"), (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmType"))
if mibBuilder.loadTexts: mepAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: mepAlarmEntry.setDescription('Every row of this table represents particular alarm.')
mepAlarmMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mepAlarmMdIndex.setStatus('current')
if mibBuilder.loadTexts: mepAlarmMdIndex.setDescription('The index to the Maintenance Domain table.')
mepAlarmMaNetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 2), Unsigned32())
if mibBuilder.loadTexts: mepAlarmMaNetIndex.setStatus('current')
if mibBuilder.loadTexts: mepAlarmMaNetIndex.setDescription('The index of the Maintenance Association Network table. ')
mepAlarmMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 3), Unsigned32())
if mibBuilder.loadTexts: mepAlarmMepIdentifier.setStatus('current')
if mibBuilder.loadTexts: mepAlarmMepIdentifier.setDescription('The index of the Maintenance Association End Point tabke. ')
mepAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 4), CfmAlarmType())
if mibBuilder.loadTexts: mepAlarmType.setStatus('current')
if mibBuilder.loadTexts: mepAlarmType.setDescription('List of all interface conditions')
mepAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 5), TrapAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mepAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: mepAlarmSeverity.setDescription('This object identifies the current severity of alarm.')
mepAlarmAffect = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 6), ServiceImpairment()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mepAlarmAffect.setStatus('current')
if mibBuilder.loadTexts: mepAlarmAffect.setDescription('This object indicates the service impairment affect of the alarm.')
mepAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mepAlarmTimeStamp.setStatus('current')
if mibBuilder.loadTexts: mepAlarmTimeStamp.setDescription('Timestamp')
alarmCfmOosDisabled = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13000)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosDisabled.setStatus('current')
if mibBuilder.loadTexts: alarmCfmOosDisabled.setDescription('Non-Specific Disablement of Management Access')
alarmCfmOosManagement = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13001)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosManagement.setStatus('current')
if mibBuilder.loadTexts: alarmCfmOosManagement.setDescription('Alarms are logged but not notified, service affecting changes are permitted')
alarmCfmOosMaintenance = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13002)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosMaintenance.setStatus('current')
if mibBuilder.loadTexts: alarmCfmOosMaintenance.setDescription('Alarms are logged but not notified, service affecting changes and operations are permitted')
alarmCfmOosAins = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13003)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmOosAins.setStatus('current')
if mibBuilder.loadTexts: alarmCfmOosAins.setDescription('Automatic In Service')
alarmCfmPriVidNotEqualExtVid = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13004)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmPriVidNotEqualExtVid.setStatus('current')
if mibBuilder.loadTexts: alarmCfmPriVidNotEqualExtVid.setDescription('The MEP PRIMARY-VID and the EXT-VID/SVID on the FLW is not equal')
alarmCfmServerSignalFailure = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13005)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmServerSignalFailure.setStatus('current')
if mibBuilder.loadTexts: alarmCfmServerSignalFailure.setDescription('All member ports signals have failed')
alarmCfmRemoteDefectIndication = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13006)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmRemoteDefectIndication.setStatus('current')
if mibBuilder.loadTexts: alarmCfmRemoteDefectIndication.setDescription('RDI')
alarmCfmCcmMacStatus = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13007)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmMacStatus.setStatus('current')
if mibBuilder.loadTexts: alarmCfmCcmMacStatus.setDescription('MAC status of the port')
alarmCfmCcmError = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13008)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmError.setStatus('current')
if mibBuilder.loadTexts: alarmCfmCcmError.setDescription('Error in the CCM received')
alarmCfmCcmLost = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13009)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmLost.setStatus('current')
if mibBuilder.loadTexts: alarmCfmCcmLost.setDescription('3 or more CCMs not recieved from far end MEP')
alarmCfmCcmXConn = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13010)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-MIB", "neEventLogTimeStamp"), ("ADVA-MIB", "neEventLogIdentityTranslation"))
if mibBuilder.loadTexts: alarmCfmCcmXConn.setStatus('current')
if mibBuilder.loadTexts: alarmCfmCcmXConn.setDescription('Cross connected CCM')
cfmExtensionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2))
cfmExtensionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1))
cfmExtensionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2))
cfmExtensionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "cfmExtensionObjectGroup"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "cfmExtensionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtensionMIBCompliance = cfmExtensionMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cfmExtensionMIBCompliance.setDescription('The compliance statement for entities implementing the ADVA FSPR7 CFM Extension MIB.')
cfmExtensionObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2, 1)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityValue"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtensionObjectGroup = cfmExtensionObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cfmExtensionObjectGroup.setDescription('A list of objects.')
cfmExtensionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2, 2)).setObjects(("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosDisabled"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosManagement"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosMaintenance"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosAins"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmPriVidNotEqualExtVid"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmServerSignalFailure"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmRemoteDefectIndication"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmMacStatus"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmError"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmLost"), ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmXConn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmExtensionNotificationGroup = cfmExtensionNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cfmExtensionNotificationGroup.setDescription('A list of notifications.')
mibBuilder.exportSymbols("ADVA-FSPR7-CFM-EXTENSION-MIB", cfmExtensionNotificationGroup=cfmExtensionNotificationGroup, mepAlarmMdIndex=mepAlarmMdIndex, alarmCfmServerSignalFailure=alarmCfmServerSignalFailure, CfmAlarmType=CfmAlarmType, alarmCfmCcmXConn=alarmCfmCcmXConn, cfmExtensionObjectGroup=cfmExtensionObjectGroup, alarmCfmCcmMacStatus=alarmCfmCcmMacStatus, mepAlarmSeverityMdIndex=mepAlarmSeverityMdIndex, cfmAlarmMIB=cfmAlarmMIB, mepAlarmTimeStamp=mepAlarmTimeStamp, alarmCfmOosAins=alarmCfmOosAins, alarmCfmCcmLost=alarmCfmCcmLost, cfmExtensionMIB=cfmExtensionMIB, cfmExtensionMIBGroups=cfmExtensionMIBGroups, alarmCfmOosMaintenance=alarmCfmOosMaintenance, mepAlarmSeverityEntry=mepAlarmSeverityEntry, cfmAlarms=cfmAlarms, mepAlarmType=mepAlarmType, mepAlarmAffect=mepAlarmAffect, alarmCfmPriVidNotEqualExtVid=alarmCfmPriVidNotEqualExtVid, cfmExtensionMIBCompliance=cfmExtensionMIBCompliance, alarmCfmOosDisabled=alarmCfmOosDisabled, cfmAlarmsPrefix=cfmAlarmsPrefix, mepAlarmSeverityTable=mepAlarmSeverityTable, mepAlarmMaNetIndex=mepAlarmMaNetIndex, mepAlarmMepIdentifier=mepAlarmMepIdentifier, alarmCfmRemoteDefectIndication=alarmCfmRemoteDefectIndication, mepAlarmSeverityMepIdentifier=mepAlarmSeverityMepIdentifier, alarmCfmCcmError=alarmCfmCcmError, mepAlarmSeverityType=mepAlarmSeverityType, PYSNMP_MODULE_ID=cfmExtensionMIB, cfmAlarmObjects=cfmAlarmObjects, alarmCfmOosManagement=alarmCfmOosManagement, cfmExtensionMIBCompliances=cfmExtensionMIBCompliances, mepAlarmTable=mepAlarmTable, mepAlarmEntry=mepAlarmEntry, mepAlarmSeverityMaNetIndex=mepAlarmSeverityMaNetIndex, cfmExtensionMIBConformance=cfmExtensionMIBConformance, mepAlarmSeverityValue=mepAlarmSeverityValue, mepAlarmSeverity=mepAlarmSeverity)
