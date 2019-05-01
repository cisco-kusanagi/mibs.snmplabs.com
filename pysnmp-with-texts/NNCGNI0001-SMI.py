#
# PySNMP MIB module NNCGNI0001-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI0001-SMI
# Produced by pysmi-0.3.4 at Wed May  1 14:15:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ModuleIdentity, Counter64, Bits, Integer32, TimeTicks, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, IpAddress, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "Counter64", "Bits", "Integer32", "TimeTicks", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "Counter32", "NotificationType")
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
    description = 'Type to be used as Unsigned32 for compatibility with SNMPv1.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NncExtCounter64(TextualConvention, OctetString):
    description = 'This defines a type that allows a 64-bit integer to be used by v1 managers and agents. Its semantics are the same as Counter64 in SNMPv2. The octets are in network-byte order.'
    status = 'current'
    displayHint = '8d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

mibBuilder.exportSymbols("NNCGNI0001-SMI", nncExtDs1=nncExtDs1, nncExtE3=nncExtE3, nncExtensions=nncExtensions, nncExtSVCSigStats=nncExtSVCSigStats, nncExtRptr=nncExtRptr, nncExtSystem=nncExtSystem, nncExtDevice=nncExtDevice, NncExtCounter64=NncExtCounter64, nncDeviceIDs=nncDeviceIDs, nncAtmStatistics=nncAtmStatistics, nncExtAlarm=nncExtAlarm, nncExtNetSynch=nncExtNetSynch, newbridge=newbridge, nncExtDiag=nncExtDiag, nncExtPmStatistics=nncExtPmStatistics, NncUnsigned32=NncUnsigned32, nncExtRestart=nncExtRestart, nncLegacyModules=nncLegacyModules, nncInterimMib=nncInterimMib, nncExtNVM=nncExtNVM, nncExtCodeSpace=nncExtCodeSpace, nncExtProbe=nncExtProbe, nncExtIntvlStats=nncExtIntvlStats, nncExtEnvironmental=nncExtEnvironmental, nncExtPosition=nncExtPosition, nncExtSyncDataCct=nncExtSyncDataCct)
