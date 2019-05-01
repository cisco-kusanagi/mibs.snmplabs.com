#
# PySNMP MIB module Dell-rlNicRedundancy (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-rlNicRedundancy
# Produced by pysmi-0.3.4 at Wed May  1 12:57:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Bits, ModuleIdentity, TimeTicks, Integer32, ObjectIdentity, Unsigned32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Bits", "ModuleIdentity", "TimeTicks", "Integer32", "ObjectIdentity", "Unsigned32", "iso", "NotificationType")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
rlNicRedundancy = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 105))
rlNicRedundancy.setRevisions(('2005-06-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlNicRedundancy.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlNicRedundancy.setLastUpdated('200506160000Z')
if mibBuilder.loadTexts: rlNicRedundancy.setOrganization('Dell')
if mibBuilder.loadTexts: rlNicRedundancy.setContactInfo('Dell.com')
if mibBuilder.loadTexts: rlNicRedundancy.setDescription('The private MIB module definition for RND NIC redundancy MIB.')
rlNicRedundancyEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 105, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlNicRedundancyEnable.setReference('')
if mibBuilder.loadTexts: rlNicRedundancyEnable.setStatus('current')
if mibBuilder.loadTexts: rlNicRedundancyEnable.setDescription('Enable / Disable NIC redundancy.')
mibBuilder.exportSymbols("Dell-rlNicRedundancy", rlNicRedundancy=rlNicRedundancy, rlNicRedundancyEnable=rlNicRedundancyEnable, PYSNMP_MODULE_ID=rlNicRedundancy)
