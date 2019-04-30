#
# PySNMP MIB module JUNIPER-MBG-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MBG-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
jnxMobileGatewayMibRoot, jnxJunosSpace = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMobileGatewayMibRoot", "jnxJunosSpace")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, MibIdentifier, Integer32, ModuleIdentity, Counter64, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, IpAddress, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter64", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "IpAddress", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxMobileGatewayPgwGgsn = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 1))
jnxMobileGatewaySgw = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2))
jnxJunosSpaceMobility = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2))
jnxJunosSpaceMobilityNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 1))
jnxJunosSpaceMobilityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2))
jnxJunosSpaceMobilityMCM = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 3))
jnxJunosSpaceMobilityMTM = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 4))
jnxJunosSpaceMobilityNotificationvars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2, 1))
mibBuilder.exportSymbols("JUNIPER-MBG-SMI", jnxJunosSpaceMobilityObjects=jnxJunosSpaceMobilityObjects, jnxJunosSpaceMobilityMCM=jnxJunosSpaceMobilityMCM, jnxJunosSpaceMobilityNotificationvars=jnxJunosSpaceMobilityNotificationvars, jnxJunosSpaceMobility=jnxJunosSpaceMobility, jnxJunosSpaceMobilityNotifications=jnxJunosSpaceMobilityNotifications, jnxMobileGatewayPgwGgsn=jnxMobileGatewayPgwGgsn, jnxJunosSpaceMobilityMTM=jnxJunosSpaceMobilityMTM, jnxMobileGatewaySgw=jnxMobileGatewaySgw)
