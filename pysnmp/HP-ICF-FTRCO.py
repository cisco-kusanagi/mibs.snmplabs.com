#
# PySNMP MIB module HP-ICF-FTRCO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-FTRCO
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter32, Counter64, Bits, Integer32, iso, IpAddress, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter32", "Counter64", "Bits", "Integer32", "iso", "IpAddress", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention, DateAndTime, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime", "RowStatus", "TruthValue")
hpicfFtrCo = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46))
hpicfFtrCo.setRevisions(('2010-06-01 00:00', '2009-08-28 00:02',))
if mibBuilder.loadTexts: hpicfFtrCo.setLastUpdated('201006010000Z')
if mibBuilder.loadTexts: hpicfFtrCo.setOrganization('HP Networking')
class VidList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '512x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(512, 512)
    fixedLength = 512

class IndexName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

hpicfFtrcoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1))
hpFtrCoEntityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1), )
if mibBuilder.loadTexts: hpFtrCoEntityTable.setStatus('current')
hpFtrCoEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1), ).setIndexNames((0, "HP-ICF-FTRCO", "hpFtrCoEntityName"))
if mibBuilder.loadTexts: hpFtrCoEntityEntry.setStatus('current')
hpFtrCoEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 1), IndexName().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpFtrCoEntityName.setStatus('current')
hpFtrCoRestrictNextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictNextIndex.setStatus('current')
hpFtrCoEntityDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpFtrCoEntityDate.setStatus('current')
hpFtrCoEntityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoEntityStatus.setStatus('current')
hpFtrCoRestrictionTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2), )
if mibBuilder.loadTexts: hpFtrCoRestrictionTable.setStatus('current')
hpFtrCoRestrictEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1), ).setIndexNames((0, "HP-ICF-FTRCO", "hpFtrCoEntityName"), (0, "HP-ICF-FTRCO", "hpFtrCoRestrictId"), (0, "HP-ICF-FTRCO", "hpFtrCoRestrictIndex"))
if mibBuilder.loadTexts: hpFtrCoRestrictEntry.setStatus('current')
hpFtrCoRestrictId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("vidIpConfig", 1), ("vidDelete", 2), ("portSecurity", 3), ("portAcl", 4), ("portSourcePortFilter", 5), ("portMeshing", 6), ("portLacp", 7), ("distributedTrunk", 8), ("portVirusThrottling", 9), ("portSflow", 10), ("portDhcpSnoop", 11), ("portLoopDetection", 12), ("portBpduPvstGuard", 13), ("qinq", 14), ("portQos", 15), ("portRateLimit", 16), ("portStaticMac", 17), ("portIpLockdown", 18), ("portIgmp", 19), ("portMirrorDestination", 20), ("portLinkConfig", 21), ("portLldp", 22), ("portKeepalive", 23), ("aclPermitLogging", 24))))
if mibBuilder.loadTexts: hpFtrCoRestrictId.setStatus('current')
hpFtrCoRestrictIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpFtrCoRestrictIndex.setStatus('current')
hpFtrCoRestrictIdParm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictIdParm.setStatus('current')
hpFtrCoRestrictStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictStatus.setStatus('current')
hpFtrCoRestrictMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictMessage.setStatus('current')
hpFtrCoRestrictPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 6), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictPorts.setStatus('current')
hpFtrCoRestrictVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 7), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictVlans.setStatus('current')
hpFtrCoExpireSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireSlot.setStatus('current')
hpFtrCoExpireApplication = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 9), IndexName().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireApplication.setStatus('current')
hpFtrCoExpireVidDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireVidDelete.setStatus('current')
hpFtrCoExpireDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 11), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireDate.setStatus('current')
hpFtrCoExpireBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireBoot.setStatus('current')
hpicfFtrCoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2))
hpicfFtrCoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 1))
hpicfFtrCoGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 2))
hpicfFtrCoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 1, 1)).setObjects(("HP-ICF-FTRCO", "hpicfFtrCoGroup"), ("HP-ICF-FTRCO", "hpicfFtrCoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFtrCoCompliance = hpicfFtrCoCompliance.setStatus('current')
hpicfFtrCoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 2, 1)).setObjects(("HP-ICF-FTRCO", "hpFtrCoRestrictNextIndex"), ("HP-ICF-FTRCO", "hpFtrCoEntityDate"), ("HP-ICF-FTRCO", "hpFtrCoEntityStatus"), ("HP-ICF-FTRCO", "hpFtrCoRestrictIdParm"), ("HP-ICF-FTRCO", "hpFtrCoRestrictStatus"), ("HP-ICF-FTRCO", "hpFtrCoRestrictMessage"), ("HP-ICF-FTRCO", "hpFtrCoRestrictPorts"), ("HP-ICF-FTRCO", "hpFtrCoRestrictVlans"), ("HP-ICF-FTRCO", "hpFtrCoExpireSlot"), ("HP-ICF-FTRCO", "hpFtrCoExpireApplication"), ("HP-ICF-FTRCO", "hpFtrCoExpireVidDelete"), ("HP-ICF-FTRCO", "hpFtrCoExpireDate"), ("HP-ICF-FTRCO", "hpFtrCoExpireBoot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFtrCoGroup = hpicfFtrCoGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-FTRCO", hpFtrCoRestrictNextIndex=hpFtrCoRestrictNextIndex, hpicfFtrCoCompliances=hpicfFtrCoCompliances, VidList=VidList, hpicfFtrCo=hpicfFtrCo, hpicfFtrCoConformance=hpicfFtrCoConformance, hpicfFtrCoGroups=hpicfFtrCoGroups, hpicfFtrCoCompliance=hpicfFtrCoCompliance, hpFtrCoEntityDate=hpFtrCoEntityDate, hpicfFtrCoGroup=hpicfFtrCoGroup, hpFtrCoExpireDate=hpFtrCoExpireDate, hpFtrCoRestrictIndex=hpFtrCoRestrictIndex, hpFtrCoRestrictEntry=hpFtrCoRestrictEntry, hpFtrCoRestrictId=hpFtrCoRestrictId, hpFtrCoEntityName=hpFtrCoEntityName, hpFtrCoExpireApplication=hpFtrCoExpireApplication, hpFtrCoRestrictionTable=hpFtrCoRestrictionTable, hpFtrCoExpireBoot=hpFtrCoExpireBoot, hpFtrCoEntityStatus=hpFtrCoEntityStatus, hpFtrCoExpireVidDelete=hpFtrCoExpireVidDelete, IndexName=IndexName, PYSNMP_MODULE_ID=hpicfFtrCo, hpFtrCoEntityTable=hpFtrCoEntityTable, hpFtrCoExpireSlot=hpFtrCoExpireSlot, hpFtrCoRestrictPorts=hpFtrCoRestrictPorts, hpFtrCoRestrictVlans=hpFtrCoRestrictVlans, hpFtrCoRestrictMessage=hpFtrCoRestrictMessage, hpicfFtrcoObjects=hpicfFtrcoObjects, hpFtrCoRestrictIdParm=hpFtrCoRestrictIdParm, hpFtrCoEntityEntry=hpFtrCoEntityEntry, hpFtrCoRestrictStatus=hpFtrCoRestrictStatus)
