#
# PySNMP MIB module CASA-CABLE-CMQUERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-CABLE-CMQUERY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32, MibIdentifier, Bits, IpAddress, NotificationType, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32", "MibIdentifier", "Bits", "IpAddress", "NotificationType", "TimeTicks", "Integer32")
TimeInterval, TruthValue, TextualConvention, DisplayString, RowStatus, TimeStamp, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TruthValue", "TextualConvention", "DisplayString", "RowStatus", "TimeStamp", "MacAddress")
casaCmQueryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 10, 18))
if mibBuilder.loadTexts: casaCmQueryMib.setLastUpdated('200809051453Z')
if mibBuilder.loadTexts: casaCmQueryMib.setOrganization('Casa Systems Inc')
class TenthdBmV(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class TenthdB(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

casaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10))
casaCmQueryMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1))
casaCmQueryTable = MibTable((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1), )
if mibBuilder.loadTexts: casaCmQueryTable.setStatus('current')
casaCmQueryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1), ).setIndexNames((0, "CASA-CABLE-CMQUERY-MIB", "casaQueryCmMacAddress"))
if mibBuilder.loadTexts: casaCmQueryEntry.setStatus('current')
casaQueryCmMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: casaQueryCmMacAddress.setStatus('current')
casaQueryCmIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmIpAddress.setStatus('current')
casaQueryCmTxTimeOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmTxTimeOffset.setStatus('current')
casaQueryCmMicroReflection = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('dBc').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmMicroReflection.setStatus('current')
casaQueryCmStatusTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 5), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmStatusTxPower.setStatus('current')
casaQueryCmStatusRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 6), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmStatusRxPower.setStatus('current')
casaQueryCmSigQSignalNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 7), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmSigQSignalNoise.setStatus('current')
casaQueryCmtsSigQSignalNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 8), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmtsSigQSignalNoise.setStatus('current')
casaCmQueryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 2))
casaCmQueryroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20858, 10, 18, 2, 1)).setObjects(("CASA-CABLE-CMQUERY-MIB", "casaQueryCmIpAddress"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmTxTimeOffset"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmMicroReflection"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusTxPower"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusRxPower"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmSigQSignalNoise"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmtsSigQSignalNoise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmQueryroup = casaCmQueryroup.setStatus('current')
casaCmQueryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 3))
casaCmQueryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 20858, 10, 18, 3, 1)).setObjects(("CASA-CABLE-CMQUERY-MIB", "casaCmQueryroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmQueryCompliance = casaCmQueryCompliance.setStatus('current')
mibBuilder.exportSymbols("CASA-CABLE-CMQUERY-MIB", casaCmQueryEntry=casaCmQueryEntry, casaQueryCmIpAddress=casaQueryCmIpAddress, casaCmQueryMib=casaCmQueryMib, PYSNMP_MODULE_ID=casaCmQueryMib, casaCmQueryroup=casaCmQueryroup, TenthdB=TenthdB, casaQueryCmMacAddress=casaQueryCmMacAddress, casaQueryCmtsSigQSignalNoise=casaQueryCmtsSigQSignalNoise, casaMgmt=casaMgmt, casaCmQueryMibObjects=casaCmQueryMibObjects, casaCmQueryTable=casaCmQueryTable, casaCmQueryCompliances=casaCmQueryCompliances, casaQueryCmSigQSignalNoise=casaQueryCmSigQSignalNoise, casaCmQueryGroups=casaCmQueryGroups, TenthdBmV=TenthdBmV, casaQueryCmMicroReflection=casaQueryCmMicroReflection, casaQueryCmStatusTxPower=casaQueryCmStatusTxPower, casaCmQueryCompliance=casaCmQueryCompliance, casaQueryCmStatusRxPower=casaQueryCmStatusRxPower, casaQueryCmTxTimeOffset=casaQueryCmTxTimeOffset)
