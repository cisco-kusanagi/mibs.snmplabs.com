#
# PySNMP MIB module TRENDMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRENDMICRO-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:27:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, ModuleIdentity, enterprises, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter32, IpAddress, Bits, NotificationType, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "enterprises", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter32", "IpAddress", "Bits", "NotificationType", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trendmicro = ModuleIdentity((1, 3, 6, 1, 4, 1, 6101))
if mibBuilder.loadTexts: trendmicro.setLastUpdated('0310101040Z')
if mibBuilder.loadTexts: trendmicro.setOrganization('Trend Micro Inc.')
if mibBuilder.loadTexts: trendmicro.setContactInfo('Trend Micro Inc. 10101 N. De Anza Blvd, Cupertino, CA - 95014, USA. Phone: + 1 (800) 228 - 5651 Web: http://www.trendmicro.com/ E-Mail: webmaster@trendmicro.com')
if mibBuilder.loadTexts: trendmicro.setDescription('Trend Micro Inc. root MIB module.')
tmNVW = MibIdentifier((1, 3, 6, 1, 4, 1, 6101, 2500))
mibBuilder.exportSymbols("TRENDMICRO-SMI", tmNVW=tmNVW, PYSNMP_MODULE_ID=trendmicro, trendmicro=trendmicro)
