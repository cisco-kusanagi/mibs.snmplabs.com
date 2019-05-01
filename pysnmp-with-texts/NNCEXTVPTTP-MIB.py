#
# PySNMP MIB module NNCEXTVPTTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCEXTVPTTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
atmVclVpi, = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nncExtensions, = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, NotificationType, Integer32, Counter32, ModuleIdentity, TimeTicks, IpAddress, MibIdentifier, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Counter32", "ModuleIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nncExtVpttp = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 80))
if mibBuilder.loadTexts: nncExtVpttp.setLastUpdated('200007211126Z')
if mibBuilder.loadTexts: nncExtVpttp.setOrganization('Alcatel Networks Corporation')
if mibBuilder.loadTexts: nncExtVpttp.setContactInfo('Alcatel CID Postal: 600 March Road Kanata, Ontario Canada K2K 2E6 Phone: +1 613 591 3600 Fax: +1 613 591 3680')
if mibBuilder.loadTexts: nncExtVpttp.setDescription("This module contains Alcatel's proprietary MIB definition for configuration of VP Trail Termination Points. This support is is provided via nncCrVpTrailTerminationPointTable. Some abreviations: VCI/Vci/vci: Virtual channel identifier VCL/Vcl/vcl: Virtual channel link VPI/Vpi/vpi: Virtual path identifier VPL/Vpl/Vpl: Virtual path link VPTTP: Virtual path trail termination point ")
nncExtVpttpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 80, 1))
nncExtVpttpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 80, 3))
nncExtVpttpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 80, 4))
nncCrVpTrailTerminationPointTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1), )
if mibBuilder.loadTexts: nncCrVpTrailTerminationPointTable.setStatus('current')
if mibBuilder.loadTexts: nncCrVpTrailTerminationPointTable.setDescription('nncCrVpTrailTerminationPointTable contains all the objects used to configure VP Trail Termination Point.')
nncCrVpTrailTerminationPointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"))
if mibBuilder.loadTexts: nncCrVpTrailTerminationPointEntry.setStatus('current')
if mibBuilder.loadTexts: nncCrVpTrailTerminationPointEntry.setDescription('An entry of nncCrVpTrailTerminationPointTable')
nncCrVpTrailTerminationPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabledWithNoAlarms", 1), ("enabledWithAlarms", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncCrVpTrailTerminationPoint.setStatus('current')
if mibBuilder.loadTexts: nncCrVpTrailTerminationPoint.setDescription(' This object is used to configure a VP Trail Termination Point. If it is enabled, the VP will be marked as VP TTP')
nncCrVpTrailTerminationPointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 80, 3, 1)).setObjects(("NNCEXTVPTTP-MIB", "nncCrVpTrailTerminationPoint"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncCrVpTrailTerminationPointGroup = nncCrVpTrailTerminationPointGroup.setStatus('current')
if mibBuilder.loadTexts: nncCrVpTrailTerminationPointGroup.setDescription('Common MIB objects for querying a PVC/SPVC Vp Trail Termination Point on Alcatel CID equipment')
nncVpttpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 123, 3, 80, 4, 1)).setObjects(("NNCEXTVPTTP-MIB", "nncCrVpTrailTerminationPointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncVpttpCompliance = nncVpttpCompliance.setStatus('current')
if mibBuilder.loadTexts: nncVpttpCompliance.setDescription('The compliance statement for Alcatel CID PVC/SPVC Vpttp MIB implementation.')
mibBuilder.exportSymbols("NNCEXTVPTTP-MIB", PYSNMP_MODULE_ID=nncExtVpttp, nncCrVpTrailTerminationPointGroup=nncCrVpTrailTerminationPointGroup, nncVpttpCompliance=nncVpttpCompliance, nncExtVpttpGroups=nncExtVpttpGroups, nncExtVpttpObjects=nncExtVpttpObjects, nncCrVpTrailTerminationPointTable=nncCrVpTrailTerminationPointTable, nncExtVpttp=nncExtVpttp, nncCrVpTrailTerminationPointEntry=nncCrVpTrailTerminationPointEntry, nncCrVpTrailTerminationPoint=nncCrVpTrailTerminationPoint, nncExtVpttpCompliances=nncExtVpttpCompliances)
