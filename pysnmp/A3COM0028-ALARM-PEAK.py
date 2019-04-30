#
# PySNMP MIB module A3COM0028-ALARM-PEAK (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0028-ALARM-PEAK
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alarmExtensions, = mibBuilder.importSymbols("A3COM0027-RMON-EXTENSIONS", "alarmExtensions")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
alarmIndex, = mibBuilder.importSymbols("RMON-MIB", "alarmIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, Unsigned32, iso, Bits, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "Unsigned32", "iso", "Bits", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alarmExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 3, 1), )
if mibBuilder.loadTexts: alarmExtTable.setStatus('mandatory')
alarmExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 3, 1, 1), ).setIndexNames((0, "RMON-MIB", "alarmIndex"))
if mibBuilder.loadTexts: alarmExtEntry.setStatus('mandatory')
alarmPeakValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPeakValue.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM0028-ALARM-PEAK", alarmExtEntry=alarmExtEntry, alarmPeakValue=alarmPeakValue, alarmExtTable=alarmExtTable)
