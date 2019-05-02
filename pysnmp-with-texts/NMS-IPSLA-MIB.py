#
# PySNMP MIB module NMS-IPSLA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-IPSLA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:22:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
nmsMgmt, = mibBuilder.importSymbols("NMS-SMI", "nmsMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, Gauge32, ObjectIdentity, Counter64, iso, NotificationType, Integer32, TimeTicks, Counter32, ModuleIdentity, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "iso", "NotificationType", "Integer32", "TimeTicks", "Counter32", "ModuleIdentity", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
nmsIpslaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102))
if mibBuilder.loadTexts: nmsIpslaMIB.setLastUpdated('20090317')
if mibBuilder.loadTexts: nmsIpslaMIB.setOrganization('')
if mibBuilder.loadTexts: nmsIpslaMIB.setContactInfo('')
if mibBuilder.loadTexts: nmsIpslaMIB.setDescription('Definition for host ')
nmsIpslaJitterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1))
ipslaJitterTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1), )
if mibBuilder.loadTexts: ipslaJitterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipslaJitterTable.setDescription('the index of ipsla udp-jitter Table.')
nmsIpslaJitterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1), ).setIndexNames((0, "NMS-IPSLA-MIB", "nmsIpslaJobEntryIndex"))
if mibBuilder.loadTexts: nmsIpslaJitterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsIpslaJitterEntry.setDescription('An entry (conceptual row) containing information about a ipsla job.')
nmsIpslaJobEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJobEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nmsIpslaJobEntryIndex.setDescription('The index for this ipsla job entry.')
nmsIpslaJobSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJobSuccesses.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJobSuccesses.setDescription("The Ipsla job entry's success times.")
nmsIpslaJobFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJobFailures.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJobFailures.setDescription("The Ipsla job entry's failure times.")
nmsIpslaJitterSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterSamples.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterSamples.setDescription("The Ipsla udp-jitter's samples .")
nmsIpslaJitterSrc2DstMin = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterSrc2DstMin.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterSrc2DstMin.setDescription('The Ipsla udp min jitter for source to destination.')
nmsIpslaJitterSrc2DstMax = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterSrc2DstMax.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterSrc2DstMax.setDescription('The Ipsla udp max jitter for source to destination.')
nmsIpslaJitterSrc2DstAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterSrc2DstAvg.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterSrc2DstAvg.setDescription('The Ipsla udp average jitter for source to destination.')
nmsIpslaJitterDst2SrcMin = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterDst2SrcMin.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterDst2SrcMin.setDescription('The Ipsla udp min jitter for destination to source.')
nmsIpslaJitterDst2SrcMax = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterDst2SrcMax.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterDst2SrcMax.setDescription('The Ipsla udp max jitter for destination to source.')
nmsIpslaJitterDst2SrcAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterDst2SrcAvg.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterDst2SrcAvg.setDescription('The Ipsla udp average jitter for destination to source.')
nmsIpslaJitterRttMin = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterRttMin.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterRttMin.setDescription("The Ipsla udp jitter's min round trip time ")
nmsIpslaJitterRttMax = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterRttMax.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterRttMax.setDescription("The Ipsla udp jitter's max round trip time ")
nmsIpslaJitterRttAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaJitterRttAvg.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaJitterRttAvg.setDescription("The Ipsla udp jitter's average round trip time ")
nmsIpslaEchoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2))
ipslaEchoTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1), )
if mibBuilder.loadTexts: ipslaEchoTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipslaEchoTable.setDescription('the index of ipsla udp-jitter Table.')
nmsIpslaEchoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1), ).setIndexNames((0, "NMS-IPSLA-MIB", "nmsIpslaEchoTargetPort"))
if mibBuilder.loadTexts: nmsIpslaEchoEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsIpslaEchoEntry.setDescription('An entry (conceptual row) containing information about a ipsla job.')
nmsIpslaEchoTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaEchoTargetPort.setStatus('mandatory')
if mibBuilder.loadTexts: nmsIpslaEchoTargetPort.setDescription("The udp echo job's target port.")
nmsIpslaEchoSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaEchoSourcePort.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaEchoSourcePort.setDescription("The udp echo job's source port.")
nmsIpslaEchoRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaEchoRtt.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaEchoRtt.setDescription("The udp echo's round trip time.")
nmsIpslaEchoProbeSent = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaEchoProbeSent.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaEchoProbeSent.setDescription('The times of the udp echo probe sent.')
nmsIpslaEchoProbeCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIpslaEchoProbeCompletion.setStatus('current')
if mibBuilder.loadTexts: nmsIpslaEchoProbeCompletion.setDescription('The times of udp echo successes.')
mibBuilder.exportSymbols("NMS-IPSLA-MIB", nmsIpslaJobSuccesses=nmsIpslaJobSuccesses, ipslaJitterTable=ipslaJitterTable, nmsIpslaJitterSamples=nmsIpslaJitterSamples, nmsIpslaEchoEntry=nmsIpslaEchoEntry, nmsIpslaJitterObjects=nmsIpslaJitterObjects, PYSNMP_MODULE_ID=nmsIpslaMIB, nmsIpslaMIB=nmsIpslaMIB, nmsIpslaJitterSrc2DstAvg=nmsIpslaJitterSrc2DstAvg, nmsIpslaJitterRttMax=nmsIpslaJitterRttMax, nmsIpslaEchoTargetPort=nmsIpslaEchoTargetPort, nmsIpslaJitterSrc2DstMin=nmsIpslaJitterSrc2DstMin, nmsIpslaJitterDst2SrcAvg=nmsIpslaJitterDst2SrcAvg, nmsIpslaEchoObjects=nmsIpslaEchoObjects, ipslaEchoTable=ipslaEchoTable, nmsIpslaEchoProbeCompletion=nmsIpslaEchoProbeCompletion, nmsIpslaJitterRttMin=nmsIpslaJitterRttMin, nmsIpslaJitterSrc2DstMax=nmsIpslaJitterSrc2DstMax, nmsIpslaEchoSourcePort=nmsIpslaEchoSourcePort, nmsIpslaJitterEntry=nmsIpslaJitterEntry, nmsIpslaEchoProbeSent=nmsIpslaEchoProbeSent, nmsIpslaJobFailures=nmsIpslaJobFailures, nmsIpslaJitterDst2SrcMax=nmsIpslaJitterDst2SrcMax, nmsIpslaJitterRttAvg=nmsIpslaJitterRttAvg, nmsIpslaEchoRtt=nmsIpslaEchoRtt, nmsIpslaJobEntryIndex=nmsIpslaJobEntryIndex, nmsIpslaJitterDst2SrcMin=nmsIpslaJitterDst2SrcMin)
