#
# PySNMP MIB module RBN-FAST-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-FAST-VRRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, MibIdentifier, TimeTicks, Unsigned32, Counter32, ObjectIdentity, Gauge32, IpAddress, Counter64, Bits, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Unsigned32", "Counter32", "ObjectIdentity", "Gauge32", "IpAddress", "Counter64", "Bits", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
VrId, = mibBuilder.importSymbols("VRRP-MIB", "VrId")
rbnFastVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 45))
rbnFastVrrpMIB.setRevisions(('2008-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnFastVrrpMIB.setRevisionsDescriptions((' Initial Version.',))
if mibBuilder.loadTexts: rbnFastVrrpMIB.setLastUpdated('200805210000Z')
if mibBuilder.loadTexts: rbnFastVrrpMIB.setOrganization('Redback Networks, Inc.')
if mibBuilder.loadTexts: rbnFastVrrpMIB.setContactInfo(' Redback Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 E-mail: mib-info@redback.com ')
if mibBuilder.loadTexts: rbnFastVrrpMIB.setDescription('This MIB describes objects used for managing Redback Fast Virtual Router Redundancy Protocol (FVRRP) routers.')
rbnFastVrrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1))
rbnFastVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2))
rbnFastVrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1), )
if mibBuilder.loadTexts: rbnFastVrrpOperTable.setStatus('current')
if mibBuilder.loadTexts: rbnFastVrrpOperTable.setDescription('A table contains rbnFastVrrpOperEntry entries')
rbnFastVrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RBN-FAST-VRRP-MIB", "rbnFastVrrpOperVrId"))
if mibBuilder.loadTexts: rbnFastVrrpOperEntry.setStatus('current')
if mibBuilder.loadTexts: rbnFastVrrpOperEntry.setDescription('Redback Fast VRRP operational characteristics entries')
rbnFastVrrpOperVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 1), VrId())
if mibBuilder.loadTexts: rbnFastVrrpOperVrId.setStatus('current')
if mibBuilder.loadTexts: rbnFastVrrpOperVrId.setDescription('This object contains the Virtual Router Identifier (VRID) of Fast VRRP routers.')
rbnFastVrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 999))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFastVrrpOperAdvertisementInterval.setStatus('current')
if mibBuilder.loadTexts: rbnFastVrrpOperAdvertisementInterval.setDescription('The Fast VRRP advertisement messages time interval. This MIB object is used to replace the standard vrrpOperAdvertisementInterval(seconds) when Fast VRRP is enabled. Either vrrpOperAdvertisementInterval or rbnFastVrrpOperAdvertisementInterval is valid based on the VRRP configurations')
rbnFastVrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1))
rbnFastVrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2))
rbnFastVrrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1, 1)).setObjects(("RBN-FAST-VRRP-MIB", "rbnFastVrrpObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFastVrrpCompliance = rbnFastVrrpCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnFastVrrpCompliance.setDescription('The compliance statement for SNMP entities which implement the Redback Fast VRRP MIB.')
rbnFastVrrpObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2, 1)).setObjects(("RBN-FAST-VRRP-MIB", "rbnFastVrrpOperAdvertisementInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFastVrrpObjectGroup = rbnFastVrrpObjectGroup.setStatus('current')
if mibBuilder.loadTexts: rbnFastVrrpObjectGroup.setDescription('The collection of objects related to Fast VRRP objects.')
mibBuilder.exportSymbols("RBN-FAST-VRRP-MIB", rbnFastVrrpConformance=rbnFastVrrpConformance, rbnFastVrrpOperEntry=rbnFastVrrpOperEntry, rbnFastVrrpOperVrId=rbnFastVrrpOperVrId, rbnFastVrrpObjectGroup=rbnFastVrrpObjectGroup, rbnFastVrrpOperTable=rbnFastVrrpOperTable, PYSNMP_MODULE_ID=rbnFastVrrpMIB, rbnFastVrrpMIB=rbnFastVrrpMIB, rbnFastVrrpOperAdvertisementInterval=rbnFastVrrpOperAdvertisementInterval, rbnFastVrrpMIBGroups=rbnFastVrrpMIBGroups, rbnFastVrrpMIBObjects=rbnFastVrrpMIBObjects, rbnFastVrrpCompliance=rbnFastVrrpCompliance, rbnFastVrrpMIBCompliances=rbnFastVrrpMIBCompliances)
