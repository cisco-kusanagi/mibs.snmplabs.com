#
# PySNMP MIB module SONICWALL-SSL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONICWALL-SSL
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Counter32, ObjectIdentity, Unsigned32, iso, NotificationType, Counter64, Bits, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Counter32", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "Counter64", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonicWALL = MibIdentifier((1, 3, 6, 1, 4, 1, 8714))
sonicSEC = ModuleIdentity((1, 3, 6, 1, 4, 1, 8714, 2))
if mibBuilder.loadTexts: sonicSEC.setLastUpdated('200203061330Z')
if mibBuilder.loadTexts: sonicSEC.setOrganization('SonicWALL, Inc.')
mibBuilder.exportSymbols("SONICWALL-SSL", sonicSEC=sonicSEC, PYSNMP_MODULE_ID=sonicSEC, sonicWALL=sonicWALL)
