#
# PySNMP MIB module CISCO-PRODUCTS-MIB-CORRECTIONS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PRODUCTS-MIB-CORRECTIONS
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoModules, ciscoProducts = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules", "ciscoProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, ModuleIdentity, Bits, Counter32, IpAddress, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Bits", "Counter32", "IpAddress", "Integer32", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoProductsMIBCorrections = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 65535))
ciscoProductsMIBCorrections.setRevisions(('2014-11-27 00:00',))
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setLastUpdated('201411270000Z')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setOrganization('The Netdisco project')
catalyst365024TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1823))
catalyst365048TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1824))
catalyst365024PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1825))
catalyst365048PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1826))
catalyst365024TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1827))
catalyst365048TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1828))
catalyst365024PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1829))
catalyst365048PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1830))
mibBuilder.exportSymbols("CISCO-PRODUCTS-MIB-CORRECTIONS", catalyst365024PD=catalyst365024PD, catalyst365024PS=catalyst365024PS, catalyst365048TS=catalyst365048TS, ciscoProductsMIBCorrections=ciscoProductsMIBCorrections, catalyst365024TD=catalyst365024TD, catalyst365048PD=catalyst365048PD, catalyst365024TS=catalyst365024TS, catalyst365048PS=catalyst365048PS, catalyst365048TD=catalyst365048TD, PYSNMP_MODULE_ID=ciscoProductsMIBCorrections)
