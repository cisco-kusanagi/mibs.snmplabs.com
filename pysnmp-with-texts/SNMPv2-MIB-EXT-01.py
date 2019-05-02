#
# PySNMP MIB module SNMPv2-MIB-EXT-01 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMPv2-MIB-EXT-01
# Produced by pysmi-0.3.4 at Wed May  1 15:08:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
system, = mibBuilder.importSymbols("SNMPv2-MIB", "system")
Counter32, IpAddress, ObjectIdentity, MibIdentifier, Integer32, Gauge32, Bits, TimeTicks, ModuleIdentity, Counter64, NotificationType, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Integer32", "Gauge32", "Bits", "TimeTicks", "ModuleIdentity", "Counter64", "NotificationType", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
sysDateAndTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 9), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDateAndTime.setStatus('current')
if mibBuilder.loadTexts: sysDateAndTime.setDescription("The locally known date and time. The value '0000000000000000'H is returned on systems without a local clock until the local date and time is learned, either from a network time protocol such as NTP or a management set operations on this object.")
mibBuilder.exportSymbols("SNMPv2-MIB-EXT-01", sysDateAndTime=sysDateAndTime)
