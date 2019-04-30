#
# PySNMP MIB module ONEACCESS-ATM-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-ATM-AAL5-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:24:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
oacRequirements, oacExpIMAtmAal5, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacRequirements", "oacExpIMAtmAal5", "oacMIBModules")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Integer32, IpAddress, Bits, Counter64, Unsigned32, NotificationType, ObjectIdentity, Counter32, TimeTicks, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "IpAddress", "Bits", "Counter64", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacAtmAal5MIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 800))
oacAtmAal5MIBModule.setRevisions(('2011-10-27 00:00', '2010-07-08 10:00',))
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setOrganization(' OneAccess ')
oacExpIMAtmAal5Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1))
oacExpIMAtmAal5Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 2))
oacExpIMAtmAal5VclLogicalIndexTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1), )
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexTable.setStatus('current')
oacExpIMAtmAal5VclLogicalIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexEntry.setStatus('current')
oacExpIMAtmAal5VclLogicalIndexIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexIfIndex.setStatus('current')
oacExpIMAtmAal5Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800))
oacExpIMAtmAal5Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800, 1))
oacExpIMAtmAal5Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800, 2))
oacExpIMAtmAal5Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 5, 800, 2, 1)).setObjects(("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5GeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMAtmAal5Compliance = oacExpIMAtmAal5Compliance.setStatus('current')
oacExpIMAtmAal5GeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 5, 800, 1, 1)).setObjects(("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5VclLogicalIndexIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMAtmAal5GeneralGroup = oacExpIMAtmAal5GeneralGroup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-ATM-AAL5-MIB", PYSNMP_MODULE_ID=oacAtmAal5MIBModule, oacExpIMAtmAal5GeneralGroup=oacExpIMAtmAal5GeneralGroup, oacExpIMAtmAal5VclLogicalIndexEntry=oacExpIMAtmAal5VclLogicalIndexEntry, oacExpIMAtmAal5Groups=oacExpIMAtmAal5Groups, oacExpIMAtmAal5Compliances=oacExpIMAtmAal5Compliances, oacExpIMAtmAal5Compliance=oacExpIMAtmAal5Compliance, oacExpIMAtmAal5Notifications=oacExpIMAtmAal5Notifications, oacExpIMAtmAal5VclLogicalIndexTable=oacExpIMAtmAal5VclLogicalIndexTable, oacExpIMAtmAal5VclLogicalIndexIfIndex=oacExpIMAtmAal5VclLogicalIndexIfIndex, oacExpIMAtmAal5Conformance=oacExpIMAtmAal5Conformance, oacAtmAal5MIBModule=oacAtmAal5MIBModule, oacExpIMAtmAal5Objects=oacExpIMAtmAal5Objects)
