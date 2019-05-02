#
# PySNMP MIB module ADTRAN-AOS-POWER (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOS-POWER
# Produced by pysmi-0.3.4 at Wed May  1 11:14:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSConformance, adGenAOSPower = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSPower")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Unsigned32, Gauge32, TimeTicks, ModuleIdentity, NotificationType, ObjectIdentity, Counter32, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Gauge32", "TimeTicks", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Counter32", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
adGenAOSPowerMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1))
adGenAOSPowerMonitor.setRevisions(('2010-09-10 00:00', '2013-02-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSPowerMonitor.setRevisionsDescriptions(('Initial version of this MIB module', 'Added EPS and RPS connection and delivery traps to the existing adGenAOSPowerTraps. Also, added the RO adGenAOSPowerEpsRpsTable to allow OID support for the changes in EPS/RPS state changes.',))
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setLastUpdated('201009100000Z')
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setContactInfo('Technical Support Dept. Postal: ADTRAN, Inc. 901 Explorer Blvd. Huntsville, AL 35806 Tel: +1 800 726-8663 Fax: +1 256 963 6217 E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setDescription('The MIB module for general configuration of power monitoring options for devices with battery backup.')
adGenAOSPowerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0))
adGenAOSPowerRollOverCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1))
adGenAOSPowerEpsRps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2))
class AdEpsPowerDeliveryStateTC(TextualConvention, Integer32):
    description = 'Indicates Failure State of a power supply '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("delivering", 1), ("notDelivering", 2), ("failed", 3), ("unknown", 4))

class AdRpsPowerDeliveryStateTC(TextualConvention, Integer32):
    description = 'Indicates Failure State of a power supply '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("failed", 1), ("busy", 2), ("delivering", 3), ("available", 4), ("unknown", 5))

class AdPowerConnectionStateTC(TextualConvention, Integer32):
    description = 'Indicates Failure State of a power supply '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("connected", 1), ("notConnected", 2), ("notApplicable", 3), ("unknown", 4))

adGenAOSPowerRolloverOnAC = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRolloverOnAC.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerRolloverOnAC.setDescription('Integer value specifying whether or not unit is on AC power.')
adGenAOSPwrRollOvrEvntSecSinceEpoch = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSPwrRollOvrEvntSecSinceEpoch.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPwrRollOvrEvntSecSinceEpoch.setDescription('The time (seconds since epoch) that a power rollover trap was generated.')
adGenAOSPowerEpsRpsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1), )
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsTable.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsTable.setDescription('EPS/RPS Power Table.')
adGenAOSPowerEpsRpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"))
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsEntry.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsEntry.setDescription('EPS/RPS entry for a particular VCID.')
adGenAOSPowerEpsRpsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsInstanceId.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsInstanceId.setDescription('Uniquely identifies a row in the adGenAOSEpsRpsTable.')
adGenAOSPowerEpsConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 2), AdPowerConnectionStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsConnectionState.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerEpsConnectionState.setDescription('Text value specifying if an EPS is connected or not.')
adGenAOSPowerEpsDeliveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 3), AdEpsPowerDeliveryStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsDeliveryState.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerEpsDeliveryState.setDescription('Text value specifying the delivery state of the EPS power.')
adGenAOSPowerRpsConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 4), AdPowerConnectionStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRpsConnectionState.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerRpsConnectionState.setDescription('Text value specifying if an RPS is connected or not.')
adGenAOSPowerRpsDeliveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 5), AdRpsPowerDeliveryStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRpsDeliveryState.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerRpsDeliveryState.setDescription('Text value specifying the delivery state of the RPS power.')
adGenAOSPowerRollover = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"), ("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"))
if mibBuilder.loadTexts: adGenAOSPowerRollover.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerRollover.setDescription('This trap indicates the unit has had a change in power source, either from AC to DC or back again. The SecSinceEpoch represents the time (seconds since epoch) that the rollover occured.')
adGenAOSEpsConnectionChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 2)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"))
if mibBuilder.loadTexts: adGenAOSEpsConnectionChange.setStatus('current')
if mibBuilder.loadTexts: adGenAOSEpsConnectionChange.setDescription('This trap indicates the unit has had a change in the EPS connection state.')
adGenAOSEpsDeliveryChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 3)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
if mibBuilder.loadTexts: adGenAOSEpsDeliveryChange.setStatus('current')
if mibBuilder.loadTexts: adGenAOSEpsDeliveryChange.setDescription('This trap indicates the unit has had a change in the EPS delivery state.')
adGenAOSRpsConnectionChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 4)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"))
if mibBuilder.loadTexts: adGenAOSRpsConnectionChange.setStatus('current')
if mibBuilder.loadTexts: adGenAOSRpsConnectionChange.setDescription('This trap indicates the unit has had a change in the RPS connection state.')
adGenAOSRpsDeliveryChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 5)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"))
if mibBuilder.loadTexts: adGenAOSRpsDeliveryChange.setStatus('current')
if mibBuilder.loadTexts: adGenAOSRpsDeliveryChange.setDescription('This trap indicates the unit has had a change in the RPS delivery state.')
adGenAOSPowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11))
adGenAOSPowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1))
adGenAOSPowerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2))
adGenAOSPowerFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRollOverCtlGroup"), ("ADTRAN-AOS-POWER", "adGenAOSPowerNotificationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSEpsRpsConfigurationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSEpsNotificationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSRpsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerFullCompliance = adGenAOSPowerFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerFullCompliance.setDescription('The compliance statement for SNMP entities which implement version 2 of the adGenAOSPower MIB. When this MIB is fully implemented, then such an implementation can claim full compliance.')
adGenAOSPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRollover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerNotificationGroup = adGenAOSPowerNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerNotificationGroup.setDescription('Trap which may be used to enhance power event driven management of the Unit.')
adGenAOSPowerRollOverCtlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 2)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerRollOverCtlGroup = adGenAOSPowerRollOverCtlGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSPowerRollOverCtlGroup.setDescription('The Unit SNMP Config Group.')
adGenAOSEpsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 3)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSEpsConnectionChange"), ("ADTRAN-AOS-POWER", "adGenAOSEpsDeliveryChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSEpsNotificationGroup = adGenAOSEpsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSEpsNotificationGroup.setDescription('Trap used to indicate state changes of EPS.')
adGenAOSRpsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 4)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSRpsConnectionChange"), ("ADTRAN-AOS-POWER", "adGenAOSRpsDeliveryChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSRpsNotificationGroup = adGenAOSRpsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSRpsNotificationGroup.setDescription('Trap used to indicate state changes of RPS.')
adGenAOSEpsRpsConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 5)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSEpsRpsConfigurationGroup = adGenAOSEpsRpsConfigurationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSEpsRpsConfigurationGroup.setDescription('The Unit SNMP Config Group.')
mibBuilder.exportSymbols("ADTRAN-AOS-POWER", adGenAOSPowerEpsConnectionState=adGenAOSPowerEpsConnectionState, adGenAOSPowerRpsConnectionState=adGenAOSPowerRpsConnectionState, adGenAOSPowerEpsRpsTable=adGenAOSPowerEpsRpsTable, AdPowerConnectionStateTC=AdPowerConnectionStateTC, AdEpsPowerDeliveryStateTC=AdEpsPowerDeliveryStateTC, adGenAOSPowerEpsRpsEntry=adGenAOSPowerEpsRpsEntry, adGenAOSPowerEpsRpsInstanceId=adGenAOSPowerEpsRpsInstanceId, adGenAOSEpsRpsConfigurationGroup=adGenAOSEpsRpsConfigurationGroup, adGenAOSPowerEpsRps=adGenAOSPowerEpsRps, adGenAOSPowerRollOverCtl=adGenAOSPowerRollOverCtl, adGenAOSRpsNotificationGroup=adGenAOSRpsNotificationGroup, adGenAOSEpsDeliveryChange=adGenAOSEpsDeliveryChange, adGenAOSPowerRollOverCtlGroup=adGenAOSPowerRollOverCtlGroup, adGenAOSPowerNotificationGroup=adGenAOSPowerNotificationGroup, adGenAOSPowerRollover=adGenAOSPowerRollover, adGenAOSPowerCompliances=adGenAOSPowerCompliances, AdRpsPowerDeliveryStateTC=AdRpsPowerDeliveryStateTC, adGenAOSPowerRolloverOnAC=adGenAOSPowerRolloverOnAC, adGenAOSRpsConnectionChange=adGenAOSRpsConnectionChange, adGenAOSPowerTraps=adGenAOSPowerTraps, PYSNMP_MODULE_ID=adGenAOSPowerMonitor, adGenAOSPwrRollOvrEvntSecSinceEpoch=adGenAOSPwrRollOvrEvntSecSinceEpoch, adGenAOSPowerFullCompliance=adGenAOSPowerFullCompliance, adGenAOSEpsNotificationGroup=adGenAOSEpsNotificationGroup, adGenAOSEpsConnectionChange=adGenAOSEpsConnectionChange, adGenAOSPowerConformance=adGenAOSPowerConformance, adGenAOSPowerMonitor=adGenAOSPowerMonitor, adGenAOSPowerGroups=adGenAOSPowerGroups, adGenAOSPowerRpsDeliveryState=adGenAOSPowerRpsDeliveryState, adGenAOSPowerEpsDeliveryState=adGenAOSPowerEpsDeliveryState, adGenAOSRpsDeliveryChange=adGenAOSRpsDeliveryChange)
