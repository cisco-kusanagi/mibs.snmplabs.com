#
# PySNMP MIB module HDSL700G2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HDSL700G2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hdsl700G2, = mibBuilder.importSymbols("GDCHDSL-MIB", "hdsl700G2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Unsigned32, Integer32, NotificationType, Counter64, Counter32, iso, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Unsigned32", "Integer32", "NotificationType", "Counter64", "Counter32", "iso", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hdsl700G2System = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 1))
hdsl700G2Version = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 1, 1))
gdc700G2SystemMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 11, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdc700G2SystemMIBversion.setStatus('mandatory')
if mibBuilder.loadTexts: gdc700G2SystemMIBversion.setDescription("Identifies the version of the MIB. The format of the version is x.yzT, where 'x' identifies the major revision number, 'y' identifies the minor revision number, 'z' identifies the typographical revision, and T identifies the test revision. Acceptable values for the individual revision components are as follows: x: 1 - 9 y: 0 - 9 z: 0 - 9 T: A - Z Upon formal release, no designation for the test revision will be present.")
hdsl700G2Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2))
hdsl700G2NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 1))
hdsl700G2DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 2))
hdsl700G2PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 3))
hdsl700G2UnitFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 4))
hdsl700G2ChecksumCorrupt = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 5))
hdsl700G2LossofSignal = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 6))
hdsl700G2UnavailableSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 7))
hdsl700G2ErrorSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 8))
hdsl700G2LossofSyncWord = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 9))
hdsl700G2LossofFrameAlign = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 10))
hdsl700G2AllOnes = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 11))
hdsl700G2RemoteLossofSig = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 12))
hdsl700G2RemoteAlarmInd = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 13))
hdsl700G2MajorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 14))
hdsl700G2MinorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 15))
mibBuilder.exportSymbols("HDSL700G2-MIB", hdsl700G2NoResponseAlm=hdsl700G2NoResponseAlm, hdsl700G2Version=hdsl700G2Version, hdsl700G2UnitFailure=hdsl700G2UnitFailure, hdsl700G2System=hdsl700G2System, hdsl700G2ErrorSec=hdsl700G2ErrorSec, hdsl700G2MinorBER=hdsl700G2MinorBER, hdsl700G2RemoteAlarmInd=hdsl700G2RemoteAlarmInd, hdsl700G2DiagRxErrAlm=hdsl700G2DiagRxErrAlm, hdsl700G2LossofSignal=hdsl700G2LossofSignal, gdc700G2SystemMIBversion=gdc700G2SystemMIBversion, hdsl700G2MajorBER=hdsl700G2MajorBER, hdsl700G2LossofFrameAlign=hdsl700G2LossofFrameAlign, hdsl700G2UnavailableSec=hdsl700G2UnavailableSec, hdsl700G2Alarms=hdsl700G2Alarms, hdsl700G2PowerUpAlm=hdsl700G2PowerUpAlm, hdsl700G2LossofSyncWord=hdsl700G2LossofSyncWord, hdsl700G2RemoteLossofSig=hdsl700G2RemoteLossofSig, hdsl700G2ChecksumCorrupt=hdsl700G2ChecksumCorrupt, hdsl700G2AllOnes=hdsl700G2AllOnes)