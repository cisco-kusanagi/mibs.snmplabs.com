#
# PySNMP MIB module JUNIPER-EX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-EX-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
jnxExMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxExMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter32, Gauge32, ObjectIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, TimeTicks, Bits, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter32", "Gauge32", "ObjectIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "TimeTicks", "Bits", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxExSwitching = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1))
jnxExAnalyzer = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1))
jnxExSecureAccessPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2))
jnxExPaeExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3))
jnxExVirtualChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4))
jnxExVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5))
jnxRPS = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6))
jnxMacNotificationRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7))
mibBuilder.exportSymbols("JUNIPER-EX-SMI", jnxExAnalyzer=jnxExAnalyzer, jnxExSecureAccessPort=jnxExSecureAccessPort, jnxExVlan=jnxExVlan, jnxExVirtualChassis=jnxExVirtualChassis, jnxExPaeExtension=jnxExPaeExtension, jnxExSwitching=jnxExSwitching, jnxRPS=jnxRPS, jnxMacNotificationRoot=jnxMacNotificationRoot)
