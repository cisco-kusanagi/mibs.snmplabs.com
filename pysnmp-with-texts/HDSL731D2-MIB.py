#
# PySNMP MIB module HDSL731D2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HDSL731D2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hdsl731D2, = mibBuilder.importSymbols("GDCHDSL-MIB", "hdsl731D2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Counter32, Counter64, iso, Integer32, TimeTicks, Bits, Gauge32, MibIdentifier, ObjectIdentity, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Counter32", "Counter64", "iso", "Integer32", "TimeTicks", "Bits", "Gauge32", "MibIdentifier", "ObjectIdentity", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hdsl731D2System = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 1))
hdsl731D2Version = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 1, 1))
gdc731D2SystemMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 11, 20, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdc731D2SystemMIBversion.setStatus('mandatory')
if mibBuilder.loadTexts: gdc731D2SystemMIBversion.setDescription("Identifies the version of the MIB. The format of the version is x.yzT, where 'x' identifies the major revision number, 'y' identifies the minor revision number, 'z' identifies the typographical revision, and T identifies the test revision. Acceptable values for the individual revision components are as follows: x: 1 - 9 y: 0 - 9 z: 0 - 9 T: A - Z Upon formal release, no designation for the test revision will be present.")
hdsl731D2Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2))
hdsl731D2NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 1))
hdsl731D2DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 2))
hdsl731D2PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 3))
hdsl731D2UnitFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 4))
hdsl731D2ChecksumCorrupt = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 5))
hdsl731D2LossofSignal = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 6))
hdsl731D2UnavailableSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 7))
hdsl731D2ErrorSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 8))
hdsl731D2LossofSyncWord = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 9))
hdsl731D2MajorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 10))
hdsl731D2MinorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 11))
mibBuilder.exportSymbols("HDSL731D2-MIB", hdsl731D2System=hdsl731D2System, gdc731D2SystemMIBversion=gdc731D2SystemMIBversion, hdsl731D2ChecksumCorrupt=hdsl731D2ChecksumCorrupt, hdsl731D2Version=hdsl731D2Version, hdsl731D2NoResponseAlm=hdsl731D2NoResponseAlm, hdsl731D2MajorBER=hdsl731D2MajorBER, hdsl731D2LossofSignal=hdsl731D2LossofSignal, hdsl731D2UnitFailure=hdsl731D2UnitFailure, hdsl731D2ErrorSec=hdsl731D2ErrorSec, hdsl731D2LossofSyncWord=hdsl731D2LossofSyncWord, hdsl731D2PowerUpAlm=hdsl731D2PowerUpAlm, hdsl731D2Alarms=hdsl731D2Alarms, hdsl731D2MinorBER=hdsl731D2MinorBER, hdsl731D2DiagRxErrAlm=hdsl731D2DiagRxErrAlm, hdsl731D2UnavailableSec=hdsl731D2UnavailableSec)
