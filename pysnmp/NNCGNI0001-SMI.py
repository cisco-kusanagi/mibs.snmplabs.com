#
# PySNMP MIB module NNCGNI0001-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI0001-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, Counter32, TimeTicks, ModuleIdentity, Gauge32, Unsigned32, IpAddress, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Counter32", "TimeTicks", "ModuleIdentity", "Gauge32", "Unsigned32", "IpAddress", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
newbridge = MibIdentifier((1, 3, 6, 1, 4, 1, 123))
nncDeviceIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1))
nncInterimMib = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 2))
nncExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3))
nncLegacyModules = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 4))
nncExtSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 1))
nncExtEnvironmental = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 2))
nncExtRestart = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 3))
nncExtCodeSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 4))
nncExtNVM = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 5))
nncExtAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 6))
nncExtNetSynch = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 7))
nncExtPosition = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 8))
nncExtDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 9))
nncExtDs1 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 10))
nncExtRptr = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 11))
nncExtProbe = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 12))
nncExtDiag = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 13))
nncExtSyncDataCct = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 14))
nncAtmStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 29))
nncExtIntvlStats = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 31))
nncExtSVCSigStats = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 32))
nncExtE3 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 40))
nncExtPmStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 65))
class NncUnsigned32(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NncExtCounter64(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

mibBuilder.exportSymbols("NNCGNI0001-SMI", nncExtAlarm=nncExtAlarm, nncDeviceIDs=nncDeviceIDs, newbridge=newbridge, NncExtCounter64=NncExtCounter64, nncExtProbe=nncExtProbe, nncLegacyModules=nncLegacyModules, nncExtDevice=nncExtDevice, nncAtmStatistics=nncAtmStatistics, nncExtEnvironmental=nncExtEnvironmental, nncExtensions=nncExtensions, nncExtNetSynch=nncExtNetSynch, nncExtDiag=nncExtDiag, nncExtPosition=nncExtPosition, nncExtSyncDataCct=nncExtSyncDataCct, nncInterimMib=nncInterimMib, nncExtRestart=nncExtRestart, nncExtE3=nncExtE3, nncExtNVM=nncExtNVM, nncExtCodeSpace=nncExtCodeSpace, NncUnsigned32=NncUnsigned32, nncExtSystem=nncExtSystem, nncExtDs1=nncExtDs1, nncExtIntvlStats=nncExtIntvlStats, nncExtRptr=nncExtRptr, nncExtPmStatistics=nncExtPmStatistics, nncExtSVCSigStats=nncExtSVCSigStats)
