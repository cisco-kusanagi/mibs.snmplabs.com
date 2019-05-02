#
# PySNMP MIB module BROCADE-MAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-MAPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Integer32, NotificationType, MibIdentifier, Counter32, ModuleIdentity, ObjectIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Integer32", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swVfId, = mibBuilder.importSymbols("SW-MIB", "swVfId")
maps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4))
maps.setRevisions(('2013-03-01 14:00', '2013-04-22 13:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: maps.setRevisionsDescriptions(('added db category', 'Updated mapsConfigObjectGroupType syntax values',))
if mibBuilder.loadTexts: maps.setLastUpdated('201304221330Z')
if mibBuilder.loadTexts: maps.setOrganization('Brocade Communications Systems, Inc.,')
if mibBuilder.loadTexts: maps.setContactInfo('Customer Support Group Brocade Communications Systems, 120 Holger Way, San Jose, CA 95134 U.S.A Tel: +1-408-392-6061 Fax: +1-408-392-6656 Email: support@Brocade.COM WEB: www.brocade.com')
if mibBuilder.loadTexts: maps.setDescription("The MIB module is for Brocade's Monitoring and Alerting Policy Suite[MAPS] feature.")
mapsTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 0))
if mibBuilder.loadTexts: mapsTraps.setStatus('current')
if mibBuilder.loadTexts: mapsTraps.setDescription('The OID represents the MAPS Trap.')
mapsConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1))
if mibBuilder.loadTexts: mapsConfig.setStatus('current')
if mibBuilder.loadTexts: mapsConfig.setDescription('The OID represents the MAPS Config params.')
mapsConfigRuleName = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigRuleName.setStatus('current')
if mibBuilder.loadTexts: mapsConfigRuleName.setDescription('It indicates the rule name which associates a condition with actions that need to be triggered when the specified condition is evaluated to true.')
mapsConfigCondition = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigCondition.setStatus('current')
if mibBuilder.loadTexts: mapsConfigCondition.setDescription('It indicates the condition defined in the rule. It includes the counter, time base and threshold value with the logical operation (eg: >, <, >= etc) that needs to be evaluated. Eg: (CRC/MIN > 10)')
mapsConfigNumOfMS = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigNumOfMS.setStatus('current')
if mibBuilder.loadTexts: mapsConfigNumOfMS.setDescription('It indicates the number of monitoring system entries in the notifications')
mapsConfigMsName = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigMsName.setStatus('current')
if mibBuilder.loadTexts: mapsConfigMsName.setDescription('This is monitoring system name like CRC, ITW, PS, FAN.')
mapsConfigObjectGroupType = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("unknown", 1), ("ps", 2), ("fan", 3), ("port", 4), ("ve-port-cir", 5), ("ts", 6), ("slot", 7), ("gbic", 8), ("flash", 9), ("rule", 10), ("switch", 11), ("chassis", 12), ("cpu", 13), ("wwn", 14), ("flow", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigObjectGroupType.setStatus('current')
if mibBuilder.loadTexts: mapsConfigObjectGroupType.setDescription('It indicates the object group type like circuit, PS, FAN.')
mapsConfigObjectKeyType = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("int32", 1), ("uint32", 2), ("float", 3), ("string", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigObjectKeyType.setStatus('current')
if mibBuilder.loadTexts: mapsConfigObjectKeyType.setDescription('It indicates the object key type. The main purpose of this object to help NMS applications to interpret the data easily. Eg: If the mapsConfigObjectGroupType is port then the key type is an integer and key value is the port number.')
mapsConfigObjectKeyValue = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigObjectKeyValue.setStatus('current')
if mibBuilder.loadTexts: mapsConfigObjectKeyValue.setDescription('It indicates the object key value. Incase of integer this field keeps as 1, 2, 3, 4, etc., and for string it keeps flowname1, flowname2, etc., Eg: if Group type is port, then the object key value is the port number.')
mapsConfigValueType = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("int32", 1), ("uint32", 2), ("float", 3), ("string", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigValueType.setStatus('current')
if mibBuilder.loadTexts: mapsConfigValueType.setDescription('It indicates the value type which could be integer, float or string. The main purpose of this object to help NMS applications to interpret the data easily.')
mapsConfigCurrentValue = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigCurrentValue.setStatus('current')
if mibBuilder.loadTexts: mapsConfigCurrentValue.setDescription('It indicates the actual value of the monitoring system.')
mapsConfigTimeBase = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigTimeBase.setStatus('current')
if mibBuilder.loadTexts: mapsConfigTimeBase.setDescription('The time period across which the change in a counter is to be monitored')
mapsConfigSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("critical", 1), ("error", 2), ("warning", 3), ("informational", 4), ("debug", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigSeverityLevel.setStatus('current')
if mibBuilder.loadTexts: mapsConfigSeverityLevel.setDescription('It indicates the severity level of the condition triggered')
mapsConfigMsList = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigMsList.setStatus('current')
if mibBuilder.loadTexts: mapsConfigMsList.setDescription('It indicates the list of the monitoring systems. The format is <msname>,<value-type>,<current-value>,<time-base> ::<msName>,<value-type>,<current-value>,<time-base>::.')
mapsConfigAction = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsConfigAction.setStatus('current')
if mibBuilder.loadTexts: mapsConfigAction.setDescription('It indicates the actions(bitmask value) that need to be triggered when the specified condition evaluated to be true. Action bitmask value mapping are none (0), raslog (1), snmp (2), port-fence (8), email (16), switchstatus-down (64), switchstatus-marginal (128), switchstatus-healthy (256), switchpolicy (512), sfp-marginal (1024) Ex: mapsConfigAction value 3 represents both raslog and snmp action')
mapsDbCategory = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapsDbCategory.setStatus('current')
if mibBuilder.loadTexts: mapsDbCategory.setDescription('indicates db category name')
mapsTrapAM = NotificationType((1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 0, 1)).setObjects(("BROCADE-MAPS-MIB", "mapsConfigRuleName"), ("BROCADE-MAPS-MIB", "mapsConfigObjectGroupType"), ("BROCADE-MAPS-MIB", "mapsConfigObjectKeyType"), ("BROCADE-MAPS-MIB", "mapsConfigObjectKeyValue"), ("BROCADE-MAPS-MIB", "mapsConfigNumOfMS"), ("BROCADE-MAPS-MIB", "mapsConfigMsList"), ("BROCADE-MAPS-MIB", "mapsConfigSeverityLevel"), ("BROCADE-MAPS-MIB", "mapsConfigCondition"), ("BROCADE-MAPS-MIB", "mapsConfigAction"), ("SW-MIB", "swVfId"), ("BROCADE-MAPS-MIB", "mapsDbCategory"))
if mibBuilder.loadTexts: mapsTrapAM.setStatus('current')
if mibBuilder.loadTexts: mapsTrapAM.setDescription('Trap to be send for MAPS threshold events.')
mibBuilder.exportSymbols("BROCADE-MAPS-MIB", mapsConfigCondition=mapsConfigCondition, maps=maps, mapsConfigRuleName=mapsConfigRuleName, mapsConfigMsName=mapsConfigMsName, mapsConfigNumOfMS=mapsConfigNumOfMS, mapsConfigObjectGroupType=mapsConfigObjectGroupType, mapsConfig=mapsConfig, mapsTrapAM=mapsTrapAM, PYSNMP_MODULE_ID=maps, mapsConfigSeverityLevel=mapsConfigSeverityLevel, mapsConfigObjectKeyValue=mapsConfigObjectKeyValue, mapsConfigAction=mapsConfigAction, mapsConfigMsList=mapsConfigMsList, mapsDbCategory=mapsDbCategory, mapsConfigTimeBase=mapsConfigTimeBase, mapsConfigCurrentValue=mapsConfigCurrentValue, mapsConfigObjectKeyType=mapsConfigObjectKeyType, mapsTraps=mapsTraps, mapsConfigValueType=mapsConfigValueType)
