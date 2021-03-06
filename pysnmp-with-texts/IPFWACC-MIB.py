#
# PySNMP MIB module IPFWACC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPFWACC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Integer32, ObjectIdentity, Gauge32, Bits, NotificationType, MibIdentifier, TimeTicks, Counter64, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Integer32", "ObjectIdentity", "Gauge32", "Bits", "NotificationType", "MibIdentifier", "TimeTicks", "Counter64", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ucdavis, ucdExperimental = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdavis", "ucdExperimental")
ipFwAccTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 1), ).setIndexNames((0, "IPFWACC-MIB", "ipFwAccIndex"))
if mibBuilder.loadTexts: ipFwAccTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccTable.setDescription('A table with the accounting rules of the IP firewall')
ipFwAccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1), ).setIndexNames((0, "IPFWACC-MIB", "ipFwAccIndex"))
if mibBuilder.loadTexts: ipFwAccEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccEntry.setDescription('An accounting rule of the IP firewall')
ipFwAccIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccIndex.setDescription('Reference index for each firewall rule.')
ipFwAccSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccSrcAddr.setDescription('The source address in the firewall rule.')
ipFwAccSrcNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccSrcNetMask.setDescription('The netmask of the source address in the firewall rule.')
ipFwAccDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccDstAddr.setDescription('The destination address in the firewall rule.')
ipFwAccDstNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccDstNetMask.setDescription('The netmask of the destination address in the firewall rule.')
ipFwAccViaName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccViaName.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccViaName.setDescription('The name of the interface to which the rule applies. If no interface is associated with the present rule, this should contain a dash (-) .')
ipFwAccViaAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccViaAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccViaAddr.setDescription('The address of the interface to which the rule applies. Using this parameter makes sense when multiple addresses are associated to the same physical interface. If not defined for the current rule this should be set to 0.')
ipFwAccProto = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("all", 2), ("tcp", 3), ("udp", 4), ("icmp", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccProto.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccProto.setDescription('The protocol(s) to which the rule applies.')
ipFwAccBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccBidir.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccBidir.setDescription('Whether the rule works in both directions (i.e. with the source and destination parts swapped) or not.')
ipFwAccDir = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("both", 1), ("in", 2), ("out", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDir.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccDir.setDescription('Whether the rule applies to packets entering or exiting the kernel.')
ipFwAccBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccBytes.setDescription('The number of bytes that matched this rule since the last reset of the counters.')
ipFwAccPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPackets.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPackets.setDescription('The number of packets that matched this rule since the last reset of the counters.')
ipFwAccNrSrcPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccNrSrcPorts.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccNrSrcPorts.setDescription('The number of ports that refer to the source address.')
ipFwAccNrDstPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccNrDstPorts.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccNrDstPorts.setDescription('The number of ports that refer to the destination address.')
ipFwAccSrcIsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("srchasrange", 1), ("srchasnorange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcIsRange.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccSrcIsRange.setDescription('Interpret the first two ports of the source part as the upper and lower limit of an interval or not.')
ipFwAccDstIsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dsthasrange", 1), ("dsthasnorange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstIsRange.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccDstIsRange.setDescription('Interpret the first two ports of the destination part as the upper and lower limit of an interval or not.')
ipFwAccPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort1.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort1.setDescription('Port number 1.')
ipFwAccPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort2.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort2.setDescription('Port number 2.')
ipFwAccPort3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort3.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort3.setDescription('Port number 3.')
ipFwAccPort4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort4.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort4.setDescription('Port number 4.')
ipFwAccPort5 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort5.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort5.setDescription('Port number 5.')
ipFwAccPort6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort6.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort6.setDescription('Port number 6.')
ipFwAccPort7 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort7.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort7.setDescription('Port number 7.')
ipFwAccPort8 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort8.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort8.setDescription('Port number 8.')
ipFwAccPort9 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort9.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort9.setDescription('Port number 9.')
ipFwAccPort10 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort10.setStatus('mandatory')
if mibBuilder.loadTexts: ipFwAccPort10.setDescription('Port number 10.')
mibBuilder.exportSymbols("IPFWACC-MIB", ipFwAccPackets=ipFwAccPackets, ipFwAccPort5=ipFwAccPort5, ipFwAccEntry=ipFwAccEntry, ipFwAccNrDstPorts=ipFwAccNrDstPorts, ipFwAccNrSrcPorts=ipFwAccNrSrcPorts, ipFwAccViaAddr=ipFwAccViaAddr, ipFwAccBidir=ipFwAccBidir, ipFwAccDstIsRange=ipFwAccDstIsRange, ipFwAccPort9=ipFwAccPort9, ipFwAccSrcAddr=ipFwAccSrcAddr, ipFwAccDstNetMask=ipFwAccDstNetMask, ipFwAccSrcNetMask=ipFwAccSrcNetMask, ipFwAccDstAddr=ipFwAccDstAddr, ipFwAccPort2=ipFwAccPort2, ipFwAccDir=ipFwAccDir, ipFwAccSrcIsRange=ipFwAccSrcIsRange, ipFwAccTable=ipFwAccTable, ipFwAccPort1=ipFwAccPort1, ipFwAccIndex=ipFwAccIndex, ipFwAccPort7=ipFwAccPort7, ipFwAccPort8=ipFwAccPort8, ipFwAccPort3=ipFwAccPort3, ipFwAccPort4=ipFwAccPort4, ipFwAccPort6=ipFwAccPort6, ipFwAccProto=ipFwAccProto, ipFwAccPort10=ipFwAccPort10, ipFwAccViaName=ipFwAccViaName, ipFwAccBytes=ipFwAccBytes)
