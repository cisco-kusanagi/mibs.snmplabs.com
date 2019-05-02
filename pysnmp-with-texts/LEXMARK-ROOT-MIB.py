#
# PySNMP MIB module LEXMARK-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEXMARK-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, NotificationType, ObjectIdentity, Counter64, TimeTicks, Integer32, Counter32, iso, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "NotificationType", "ObjectIdentity", "Counter64", "TimeTicks", "Integer32", "Counter32", "iso", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lexmarkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 4, 1))
lexmarkMIB.setRevisions(('2010-12-01 23:00', '2009-11-24 20:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lexmarkMIB.setRevisionsDescriptions(('Version 1.0.0 of the LEXMARK-ROOT-MIB', 'Version 0.0.1 Initial release of LEXMARK-ROOT-MIB',))
if mibBuilder.loadTexts: lexmarkMIB.setLastUpdated('201012012300Z')
if mibBuilder.loadTexts: lexmarkMIB.setOrganization('Lexmark International, Inc.')
if mibBuilder.loadTexts: lexmarkMIB.setContactInfo('snmpmib@lexmark.com')
if mibBuilder.loadTexts: lexmarkMIB.setDescription('The root mib Module for Lexmark International Copyright 2009 Lexmark International')
lexmark = MibIdentifier((1, 3, 6, 1, 4, 1, 641))
lexmarkModules = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 4))
lexmarkMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 5))
mibBuilder.exportSymbols("LEXMARK-ROOT-MIB", lexmarkModules=lexmarkModules, lexmarkMibObjects=lexmarkMibObjects, lexmarkMIB=lexmarkMIB, PYSNMP_MODULE_ID=lexmarkMIB, lexmark=lexmark)
