#
# PySNMP MIB module NETASQ-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETASQ-SMI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, TimeTicks, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, NotificationType, IpAddress, Gauge32, ObjectIdentity, Unsigned32, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "TimeTicks", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "NotificationType", "IpAddress", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter64", "enterprises")
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
mibBuilder.exportSymbols("NETASQ-SMI-MIB", ntqUsers=ntqUsers, ntqNotifications=ntqNotifications, netasq=netasq, netasqMIB=netasqMIB, ntqif=ntqif, ntqVPN=ntqVPN, ntqProductProperty=ntqProductProperty, ntqAlarm=ntqAlarm, ntqHosts=ntqHosts)
