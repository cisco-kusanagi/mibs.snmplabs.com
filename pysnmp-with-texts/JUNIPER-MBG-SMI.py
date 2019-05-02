#
# PySNMP MIB module JUNIPER-MBG-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MBG-SMI
# Produced by pysmi-0.3.4 at Wed May  1 14:00:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
jnxMobileGatewayMibRoot, jnxJunosSpace = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMobileGatewayMibRoot", "jnxJunosSpace")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter64, Bits, Gauge32, iso, Counter32, NotificationType, ObjectIdentity, TimeTicks, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter64", "Bits", "Gauge32", "iso", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxMobileGatewayPgwGgsn = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 1))
jnxMobileGatewaySgw = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2))
jnxJunosSpaceMobility = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2))
jnxJunosSpaceMobilityNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 1))
jnxJunosSpaceMobilityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2))
jnxJunosSpaceMobilityMCM = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 3))
jnxJunosSpaceMobilityMTM = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 4))
jnxJunosSpaceMobilityNotificationvars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2, 1))
mibBuilder.exportSymbols("JUNIPER-MBG-SMI", jnxJunosSpaceMobilityMTM=jnxJunosSpaceMobilityMTM, jnxMobileGatewayPgwGgsn=jnxMobileGatewayPgwGgsn, jnxJunosSpaceMobilityNotifications=jnxJunosSpaceMobilityNotifications, jnxJunosSpaceMobility=jnxJunosSpaceMobility, jnxMobileGatewaySgw=jnxMobileGatewaySgw, jnxJunosSpaceMobilityObjects=jnxJunosSpaceMobilityObjects, jnxJunosSpaceMobilityMCM=jnxJunosSpaceMobilityMCM, jnxJunosSpaceMobilityNotificationvars=jnxJunosSpaceMobilityNotificationvars)
