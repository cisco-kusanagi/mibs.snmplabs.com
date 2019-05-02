#
# PySNMP MIB module IRONPORT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IRONPORT-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:29:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, Bits, NotificationType, TimeTicks, Gauge32, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, ObjectIdentity, Integer32, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Bits", "NotificationType", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Integer32", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ironPort = MibIdentifier((1, 3, 6, 1, 4, 1, 15497))
asyncOSAppliances = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1))
asyncOSMail = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1, 1))
asyncOSWebSecurityAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1, 2))
mibBuilder.exportSymbols("IRONPORT-SMI", asyncOSMail=asyncOSMail, asyncOSWebSecurityAppliance=asyncOSWebSecurityAppliance, ironPort=ironPort, asyncOSAppliances=asyncOSAppliances)
