#
# PySNMP MIB module SNMPv2-MIB-EXT-01 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMPv2-MIB-EXT-01
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
system, = mibBuilder.importSymbols("SNMPv2-MIB", "system")
NotificationType, Counter32, Integer32, Gauge32, Counter64, ModuleIdentity, iso, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Integer32", "Gauge32", "Counter64", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "MibIdentifier", "Bits")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
sysDateAndTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 9), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDateAndTime.setStatus('current')
mibBuilder.exportSymbols("SNMPv2-MIB-EXT-01", sysDateAndTime=sysDateAndTime)
