#
# PySNMP MIB module A3COM0028-ALARM-PEAK (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0028-ALARM-PEAK
# Produced by pysmi-0.3.4 at Wed May  1 11:08:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alarmExtensions, = mibBuilder.importSymbols("A3COM0027-RMON-EXTENSIONS", "alarmExtensions")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
alarmIndex, = mibBuilder.importSymbols("RMON-MIB", "alarmIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Counter64, Unsigned32, IpAddress, NotificationType, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Counter64", "Unsigned32", "IpAddress", "NotificationType", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alarmExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 3, 1), )
if mibBuilder.loadTexts: alarmExtTable.setStatus('mandatory')
if mibBuilder.loadTexts: alarmExtTable.setDescription('This table augments the RMON alarm table defined in RFC1757. The table does not define its own indices, but rather shares those defined for the RMON alarm table. For each entry in the RMON alarm table there will be a row in this table. The columns in this table can be considered as additions to the standard MIB.')
alarmExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 3, 1, 1), ).setIndexNames((0, "RMON-MIB", "alarmIndex"))
if mibBuilder.loadTexts: alarmExtEntry.setStatus('mandatory')
if mibBuilder.loadTexts: alarmExtEntry.setDescription('')
alarmPeakValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPeakValue.setStatus('mandatory')
if mibBuilder.loadTexts: alarmPeakValue.setDescription("This value reports the maximum calculated value of 'alarmValue' since the alarm was last activiated.This value can be used by auto-calibrate applications.")
mibBuilder.exportSymbols("A3COM0028-ALARM-PEAK", alarmExtTable=alarmExtTable, alarmExtEntry=alarmExtEntry, alarmPeakValue=alarmPeakValue)
