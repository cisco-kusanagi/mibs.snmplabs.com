#
# PySNMP MIB module JUNIPER-EX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-EX-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:58:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
jnxExMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxExMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32, ModuleIdentity, MibIdentifier, Counter64, IpAddress, NotificationType, TimeTicks, ObjectIdentity, Integer32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32", "ModuleIdentity", "MibIdentifier", "Counter64", "IpAddress", "NotificationType", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxExSwitching = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1))
jnxExAnalyzer = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1))
jnxExSecureAccessPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2))
jnxExPaeExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3))
jnxExVirtualChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4))
jnxExVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5))
jnxRPS = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6))
jnxMacNotificationRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7))
mibBuilder.exportSymbols("JUNIPER-EX-SMI", jnxExSwitching=jnxExSwitching, jnxExAnalyzer=jnxExAnalyzer, jnxExSecureAccessPort=jnxExSecureAccessPort, jnxExVlan=jnxExVlan, jnxExVirtualChassis=jnxExVirtualChassis, jnxExPaeExtension=jnxExPaeExtension, jnxMacNotificationRoot=jnxMacNotificationRoot, jnxRPS=jnxRPS)
