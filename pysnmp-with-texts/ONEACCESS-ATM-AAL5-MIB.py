#
# PySNMP MIB module ONEACCESS-ATM-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-ATM-AAL5-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
oacExpIMAtmAal5, oacRequirements, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMAtmAal5", "oacRequirements", "oacMIBModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, NotificationType, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Counter64, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter64", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacAtmAal5MIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 800))
oacAtmAal5MIBModule.setRevisions(('2011-10-27 00:00', '2010-07-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacAtmAal5MIBModule.setRevisionsDescriptions(('Fixed compilation errors and warnings.', 'This MIB module describes ATM AAL5 objects.',))
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setDescription('Contact updated')
oacExpIMAtmAal5Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1))
oacExpIMAtmAal5Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 2))
oacExpIMAtmAal5VclLogicalIndexTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1), )
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexTable.setStatus('current')
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexTable.setDescription(' Table to get a link between Port/Vp/Vc and OneOs ifTable index of logical interface')
oacExpIMAtmAal5VclLogicalIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexEntry.setStatus('current')
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexEntry.setDescription(' indexes are taken from atmVclTable ')
oacExpIMAtmAal5VclLogicalIndexIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexIfIndex.setStatus('current')
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexIfIndex.setDescription('The ifTable index of the ATM logical port interface associated with the VP/VC.')
oacExpIMAtmAal5Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800))
oacExpIMAtmAal5Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800, 1))
oacExpIMAtmAal5Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800, 2))
oacExpIMAtmAal5Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 5, 800, 2, 1)).setObjects(("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5GeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMAtmAal5Compliance = oacExpIMAtmAal5Compliance.setStatus('current')
if mibBuilder.loadTexts: oacExpIMAtmAal5Compliance.setDescription('The compliance statement for agents that support the ONEACCESS-ATM-AAL5-MIB.')
oacExpIMAtmAal5GeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 5, 800, 1, 1)).setObjects(("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5VclLogicalIndexIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMAtmAal5GeneralGroup = oacExpIMAtmAal5GeneralGroup.setStatus('current')
if mibBuilder.loadTexts: oacExpIMAtmAal5GeneralGroup.setDescription('This group is mandatory for ATM AAL5 entity.')
mibBuilder.exportSymbols("ONEACCESS-ATM-AAL5-MIB", oacExpIMAtmAal5Groups=oacExpIMAtmAal5Groups, oacExpIMAtmAal5Compliances=oacExpIMAtmAal5Compliances, oacAtmAal5MIBModule=oacAtmAal5MIBModule, oacExpIMAtmAal5VclLogicalIndexIfIndex=oacExpIMAtmAal5VclLogicalIndexIfIndex, oacExpIMAtmAal5Compliance=oacExpIMAtmAal5Compliance, oacExpIMAtmAal5VclLogicalIndexTable=oacExpIMAtmAal5VclLogicalIndexTable, oacExpIMAtmAal5Conformance=oacExpIMAtmAal5Conformance, oacExpIMAtmAal5VclLogicalIndexEntry=oacExpIMAtmAal5VclLogicalIndexEntry, oacExpIMAtmAal5GeneralGroup=oacExpIMAtmAal5GeneralGroup, oacExpIMAtmAal5Objects=oacExpIMAtmAal5Objects, PYSNMP_MODULE_ID=oacAtmAal5MIBModule, oacExpIMAtmAal5Notifications=oacExpIMAtmAal5Notifications)
