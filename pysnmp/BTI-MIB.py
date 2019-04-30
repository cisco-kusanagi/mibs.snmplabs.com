#
# PySNMP MIB module BTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, Bits, Unsigned32, MibIdentifier, TimeTicks, iso, NotificationType, ModuleIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Bits", "Unsigned32", "MibIdentifier", "TimeTicks", "iso", "NotificationType", "ModuleIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
btiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 1, 1))
btiMib.setRevisions(('2012-11-30 12:00', '2012-03-09 12:00', '2012-02-10 12:00', '2011-09-26 12:00', '2008-05-30 12:00', '2007-08-27 12:00', '2005-07-25 12:00', '2004-09-23 12:00', '2003-12-01 12:00',))
if mibBuilder.loadTexts: btiMib.setLastUpdated('201211301200Z')
if mibBuilder.loadTexts: btiMib.setOrganization('BTI Systems Inc.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 18070))
btiModules = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 1))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2))
bti7000 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 2))
btiems = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 4))
btiPSM = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 6))
widecastCache = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 7))
bti800 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 8))
bti7800 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 9))
mibBuilder.exportSymbols("BTI-MIB", btiems=btiems, btiSystems=btiSystems, btiMib=btiMib, PYSNMP_MODULE_ID=btiMib, bti7800=bti7800, btiPSM=btiPSM, bti800=bti800, widecastCache=widecastCache, btiProducts=btiProducts, bti7000=bti7000, btiModules=btiModules)
