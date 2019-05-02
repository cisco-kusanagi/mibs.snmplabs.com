#
# PySNMP MIB module CASA-CABLE-CMQUERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-CABLE-CMQUERY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, MibIdentifier, IpAddress, Bits, Integer32, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "Bits", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity")
TimeInterval, TimeStamp, DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TimeStamp", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
casaCmQueryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 10, 18))
if mibBuilder.loadTexts: casaCmQueryMib.setLastUpdated('200809051453Z')
if mibBuilder.loadTexts: casaCmQueryMib.setOrganization('Casa Systems Inc')
if mibBuilder.loadTexts: casaCmQueryMib.setContactInfo('Guangzhou Casa Communications Ltd. No.206 YueHe Bld,Huacui Str. Tianhe Industrial Park Guangzhou TEL:020 85545002/85577786 ext.212 FAX:020 85545002 ext.230 E-mail: huangxiaole@casachina.com.cn ')
if mibBuilder.loadTexts: casaCmQueryMib.setDescription('This is the enterprise MIB Module for CASA systems CMTS.')
class TenthdBmV(TextualConvention, Integer32):
    description = 'This data type represents power levels that are normally expressed in dBmV. Units are in tenths of a dBmV; for example, 5.1 dBmV will be represented as 51.'
    status = 'current'
    displayHint = 'd-1'

class TenthdB(TextualConvention, Integer32):
    description = 'This data type represents power levels that are normally expressed in dB. Units are in tenths of a dB; for example, 5.1 dB will be represented as 51.'
    status = 'current'
    displayHint = 'd-1'

casaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10))
casaCmQueryMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1))
casaCmQueryTable = MibTable((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1), )
if mibBuilder.loadTexts: casaCmQueryTable.setStatus('current')
if mibBuilder.loadTexts: casaCmQueryTable.setDescription('describes the PHY signal quality and Tx/Rx parameter of cable modem. ')
casaCmQueryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1), ).setIndexNames((0, "CASA-CABLE-CMQUERY-MIB", "casaQueryCmMacAddress"))
if mibBuilder.loadTexts: casaCmQueryEntry.setStatus('current')
if mibBuilder.loadTexts: casaCmQueryEntry.setDescription('describes the PHY signal quality and Tx/Rx parameter of cable modem,index of this table is casaQueryCmMacAddress. ')
casaQueryCmMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: casaQueryCmMacAddress.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmMacAddress.setDescription('The cable modem Mac Address. ')
casaQueryCmIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmIpAddress.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmIpAddress.setDescription('The cable modem Ip Address. ')
casaQueryCmTxTimeOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmTxTimeOffset.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmTxTimeOffset.setDescription('A measure of the current round trip time at the CM, or the maximum round trip time seen by the CMTS. Used for timing of CM upstream transmissions to ensure synchronized arrivals at the CMTS. Units are in terms of (6.25 microseconds/64).')
casaQueryCmMicroReflection = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('dBc').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmMicroReflection.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmMicroReflection.setDescription('Total microreflections including in-channel response as perceived on this interface, measured in dBc below the signal level. This object is not assumed to return an absolutely accurate value, but should give a rough indication of microreflections received on this interface. It is up to the implementor to provide information as accurate as possible. ')
casaQueryCmStatusTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 5), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmStatusTxPower.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmStatusTxPower.setDescription('The operational transmit power of the cable modem downstream channel,the most current value (CM) or the value of 0. ')
casaQueryCmStatusRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 6), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmStatusRxPower.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmStatusRxPower.setDescription('The operational receive power of the cable modem upstream channel,the most current value (CM) or the value of 0')
casaQueryCmSigQSignalNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 7), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmSigQSignalNoise.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmSigQSignalNoise.setDescription('Signal/Noise ratio as perceived for this channel. describes the Signal/Noise of the upstream channel of CM . ')
casaQueryCmtsSigQSignalNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 8), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmtsSigQSignalNoise.setStatus('current')
if mibBuilder.loadTexts: casaQueryCmtsSigQSignalNoise.setDescription('Signal/Noise ratio as perceived for this channel. describes the average Signal/Noiseof the upstream channel of CMTS. ')
casaCmQueryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 2))
casaCmQueryroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20858, 10, 18, 2, 1)).setObjects(("CASA-CABLE-CMQUERY-MIB", "casaQueryCmIpAddress"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmTxTimeOffset"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmMicroReflection"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusTxPower"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusRxPower"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmSigQSignalNoise"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmtsSigQSignalNoise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmQueryroup = casaCmQueryroup.setStatus('current')
if mibBuilder.loadTexts: casaCmQueryroup.setDescription('Box is required to support objects in this group ')
casaCmQueryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 3))
casaCmQueryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 20858, 10, 18, 3, 1)).setObjects(("CASA-CABLE-CMQUERY-MIB", "casaCmQueryroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmQueryCompliance = casaCmQueryCompliance.setStatus('current')
if mibBuilder.loadTexts: casaCmQueryCompliance.setDescription('Description.')
mibBuilder.exportSymbols("CASA-CABLE-CMQUERY-MIB", casaQueryCmIpAddress=casaQueryCmIpAddress, casaCmQueryEntry=casaCmQueryEntry, casaCmQueryroup=casaCmQueryroup, casaCmQueryMib=casaCmQueryMib, casaCmQueryCompliance=casaCmQueryCompliance, TenthdB=TenthdB, casaCmQueryGroups=casaCmQueryGroups, TenthdBmV=TenthdBmV, casaQueryCmMacAddress=casaQueryCmMacAddress, casaCmQueryTable=casaCmQueryTable, casaQueryCmtsSigQSignalNoise=casaQueryCmtsSigQSignalNoise, casaQueryCmStatusTxPower=casaQueryCmStatusTxPower, PYSNMP_MODULE_ID=casaCmQueryMib, casaMgmt=casaMgmt, casaQueryCmTxTimeOffset=casaQueryCmTxTimeOffset, casaQueryCmSigQSignalNoise=casaQueryCmSigQSignalNoise, casaCmQueryMibObjects=casaCmQueryMibObjects, casaCmQueryCompliances=casaCmQueryCompliances, casaQueryCmStatusRxPower=casaQueryCmStatusRxPower, casaQueryCmMicroReflection=casaQueryCmMicroReflection)
