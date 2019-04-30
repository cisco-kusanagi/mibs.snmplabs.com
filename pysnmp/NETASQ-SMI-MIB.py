#
# PySNMP MIB module NETASQ-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETASQ-SMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, IpAddress, TimeTicks, Counter64, Gauge32, Integer32, NotificationType, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter64", "Gauge32", "Integer32", "NotificationType", "enterprises", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netasq = MibIdentifier((1, 3, 6, 1, 4, 1, 11256))
netasqMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1))
ntqProductProperty = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 0))
ntqVPN = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 1))
ntqUsers = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 2))
ntqHosts = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 3))
ntqif = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 4))
ntqAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 5))
ntqNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 6))
mibBuilder.exportSymbols("NETASQ-SMI-MIB", ntqAlarm=ntqAlarm, ntqUsers=ntqUsers, netasqMIB=netasqMIB, ntqVPN=ntqVPN, ntqHosts=ntqHosts, ntqNotifications=ntqNotifications, ntqProductProperty=ntqProductProperty, netasq=netasq, ntqif=ntqif)
