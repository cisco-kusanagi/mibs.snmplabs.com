#
# PySNMP MIB module TRENDMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRENDMICRO-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Gauge32, ObjectIdentity, Counter32, NotificationType, IpAddress, iso, ModuleIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "NotificationType", "IpAddress", "iso", "ModuleIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trendmicro = ModuleIdentity((1, 3, 6, 1, 4, 1, 6101))
if mibBuilder.loadTexts: trendmicro.setLastUpdated('0310101040Z')
if mibBuilder.loadTexts: trendmicro.setOrganization('Trend Micro Inc.')
tmNVW = MibIdentifier((1, 3, 6, 1, 4, 1, 6101, 2500))
mibBuilder.exportSymbols("TRENDMICRO-SMI", tmNVW=tmNVW, PYSNMP_MODULE_ID=trendmicro, trendmicro=trendmicro)
