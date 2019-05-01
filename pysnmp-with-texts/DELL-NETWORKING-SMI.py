#
# PySNMP MIB module DELL-NETWORKING-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-NETWORKING-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:37:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, enterprises, Counter64, Counter32, Gauge32, Unsigned32, MibIdentifier, iso, TimeTicks, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "enterprises", "Counter64", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "iso", "TimeTicks", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dellNet = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027))
dellNet.setRevisions(('2007-06-15 12:00', '1900-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dellNet.setRevisionsDescriptions(('Added dellNetModules.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: dellNet.setLastUpdated('200706151200Z')
if mibBuilder.loadTexts: dellNet.setOrganization('Dell Inc')
if mibBuilder.loadTexts: dellNet.setContactInfo('http://www.dell.com/support')
if mibBuilder.loadTexts: dellNet.setDescription('The Structure of Management Information for the Dell Networking OS.')
dellNetProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 1))
if mibBuilder.loadTexts: dellNetProducts.setStatus('current')
if mibBuilder.loadTexts: dellNetProducts.setDescription("Dell Networking OS Products' OID.")
dellNetCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 2))
if mibBuilder.loadTexts: dellNetCommon.setStatus('current')
if mibBuilder.loadTexts: dellNetCommon.setDescription('All Dell Networking OS shared TEXTTUAL-CONVENTION definitions')
dellNetMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 3))
if mibBuilder.loadTexts: dellNetMgmt.setStatus('current')
if mibBuilder.loadTexts: dellNetMgmt.setDescription('dellNetMgmt is the main subtree for Dell Networking OS mib development.')
dellNetModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 4))
if mibBuilder.loadTexts: dellNetModules.setStatus('current')
if mibBuilder.loadTexts: dellNetModules.setDescription('dellNetModules provides a root object identifier from which MODULE-IDENTITY values may be based.')
dellNetExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 20))
if mibBuilder.loadTexts: dellNetExperiment.setStatus('current')
if mibBuilder.loadTexts: dellNetExperiment.setDescription('dellNetExperiment provides a root object identifier from which experimental mibs may be temporarily based. mibs are typicially based here if they fall in one of two categories 1) are IETF work-in-process mibs which have not been assigned a permanent object identifier by the IANA. 2) are Dell Networking OS work-in-process which has not been assigned a permanent object identifier by the Dell Networking OS assigned number authority, typicially because the mib is not ready for deployment. NOTE WELL: support for mibs in the dellNetExperiment subtree will be deleted when a permanent object identifier assignment is made.')
mibBuilder.exportSymbols("DELL-NETWORKING-SMI", dellNetMgmt=dellNetMgmt, dellNetExperiment=dellNetExperiment, PYSNMP_MODULE_ID=dellNet, dellNetCommon=dellNetCommon, dellNet=dellNet, dellNetProducts=dellNetProducts, dellNetModules=dellNetModules)
