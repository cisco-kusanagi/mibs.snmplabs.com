#
# PySNMP MIB module BTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Gauge32, IpAddress, NotificationType, iso, Unsigned32, enterprises, Integer32, MibIdentifier, ModuleIdentity, Counter32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Gauge32", "IpAddress", "NotificationType", "iso", "Unsigned32", "enterprises", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter32", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
btiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 1, 1))
btiMib.setRevisions(('2012-11-30 12:00', '2012-03-09 12:00', '2012-02-10 12:00', '2011-09-26 12:00', '2008-05-30 12:00', '2007-08-27 12:00', '2005-07-25 12:00', '2004-09-23 12:00', '2003-12-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: btiMib.setRevisionsDescriptions(('Added identifier for the bti7800 product.', 'Added identifiers for btiHoard, bti800 branches.', 'Moved PSM to btiProducts 6, to avoid PVX overlap.', 'Added btiPSM node.', 'Changed name of netstender node to bti7000. Removed obsolete ols node.', 'Added btiems node.', 'Updated Contact Info in Module Identity', 'MIB Updated for Netstender Rel 3.0: Updated object hierarchy to support Netstender 1030 - name of object identifier netstender2060 generalized to netstender', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: btiMib.setLastUpdated('201211301200Z')
if mibBuilder.loadTexts: btiMib.setOrganization('BTI Systems Inc.')
if mibBuilder.loadTexts: btiMib.setContactInfo('Technical Support BTI Systems Inc. 200-1000 Innovation Dr. Kanata, Ontario, Canada K2K 3E7 (613) 287-1700 support@btisystems.com')
if mibBuilder.loadTexts: btiMib.setDescription('This is a top-level MIB for BTI whose purpose is to lay out the top-level objects in the OID hierarchy')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 18070))
btiModules = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 1))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2))
bti7000 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 2))
btiems = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 4))
btiPSM = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 6))
widecastCache = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 7))
bti800 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 8))
bti7800 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 9))
mibBuilder.exportSymbols("BTI-MIB", bti800=bti800, bti7800=bti7800, widecastCache=widecastCache, bti7000=bti7000, btiems=btiems, btiMib=btiMib, btiModules=btiModules, btiPSM=btiPSM, btiProducts=btiProducts, PYSNMP_MODULE_ID=btiMib, btiSystems=btiSystems)
