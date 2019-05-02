#
# PySNMP MIB module A3COM0027-RMON-EXTENSIONS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0027-RMON-EXTENSIONS
# Produced by pysmi-0.3.4 at Wed May  1 11:08:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
rmonExtensions, = mibBuilder.importSymbols("A3COM0004-GENERIC", "rmonExtensions")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ObjectIdentity, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, Counter64, iso, Counter32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ObjectIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter64", "iso", "Counter32", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
remotePoll = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25, 1))
hostExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25, 2))
alarmExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25, 3))
eventExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25, 4))
command = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25, 5))
probeConfigNetExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25, 6))
mibBuilder.exportSymbols("A3COM0027-RMON-EXTENSIONS", remotePoll=remotePoll, probeConfigNetExtensions=probeConfigNetExtensions, hostExtensions=hostExtensions, eventExtensions=eventExtensions, command=command, alarmExtensions=alarmExtensions)
