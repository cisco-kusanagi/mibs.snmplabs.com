#
# PySNMP MIB module NTWS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, MibIdentifier, ObjectIdentity, Counter64, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, Integer32, iso, Counter32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter64", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "Integer32", "iso", "Counter32", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1))
ntwsRootMib.setRevisions(('2007-08-15 00:04', '2006-03-31 00:03', '2005-04-21 00:00',))
if mibBuilder.loadTexts: ntwsRootMib.setLastUpdated('200708150004Z')
if mibBuilder.loadTexts: ntwsRootMib.setOrganization('Nortel Networks')
ntwsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 1))
ntwsTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 2))
ntwsRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3))
ntwsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4))
ntwsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 5))
mibBuilder.exportSymbols("NTWS-ROOT-MIB", ntwsTemporary=ntwsTemporary, ntwsProducts=ntwsProducts, ntwsRootMib=ntwsRootMib, ntwsTraps=ntwsTraps, ntwsRegistration=ntwsRegistration, ntwsMibs=ntwsMibs, PYSNMP_MODULE_ID=ntwsRootMib)
