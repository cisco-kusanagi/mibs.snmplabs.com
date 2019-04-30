#
# PySNMP MIB module LEXMARK-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEXMARK-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, iso, Counter64, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, NotificationType, IpAddress, Gauge32, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "iso", "Counter64", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "NotificationType", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lexmarkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 4, 1))
lexmarkMIB.setRevisions(('2010-12-01 23:00', '2009-11-24 20:40',))
if mibBuilder.loadTexts: lexmarkMIB.setLastUpdated('201012012300Z')
if mibBuilder.loadTexts: lexmarkMIB.setOrganization('Lexmark International, Inc.')
lexmark = MibIdentifier((1, 3, 6, 1, 4, 1, 641))
lexmarkModules = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 4))
lexmarkMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 5))
mibBuilder.exportSymbols("LEXMARK-ROOT-MIB", lexmark=lexmark, lexmarkModules=lexmarkModules, PYSNMP_MODULE_ID=lexmarkMIB, lexmarkMibObjects=lexmarkMibObjects, lexmarkMIB=lexmarkMIB)
