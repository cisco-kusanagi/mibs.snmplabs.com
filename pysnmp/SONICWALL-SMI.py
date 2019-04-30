#
# PySNMP MIB module SONICWALL-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONICWALL-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, Unsigned32, NotificationType, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, enterprises, IpAddress, iso, MibIdentifier, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "enterprises", "IpAddress", "iso", "MibIdentifier", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonicwall = ModuleIdentity((1, 3, 6, 1, 4, 1, 8741))
sonicwall.setRevisions(('2003-04-22 00:00',))
if mibBuilder.loadTexts: sonicwall.setLastUpdated('200304220000Z')
if mibBuilder.loadTexts: sonicwall.setOrganization('SonicWall, Inc.')
sonicwallFw = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 1))
if mibBuilder.loadTexts: sonicwallFw.setStatus('current')
mibBuilder.exportSymbols("SONICWALL-SMI", sonicwallFw=sonicwallFw, PYSNMP_MODULE_ID=sonicwall, sonicwall=sonicwall)
