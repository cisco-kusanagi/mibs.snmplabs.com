#
# PySNMP MIB module ZHONE-COM-IP-ICMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-IP-ICMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:47:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, Gauge32, ModuleIdentity, Integer32, Unsigned32, Counter64, iso, ObjectIdentity, MibIdentifier, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Gauge32", "ModuleIdentity", "Integer32", "Unsigned32", "Counter64", "iso", "ObjectIdentity", "MibIdentifier", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdEntry, = mibBuilder.importSymbols("ZHONE-COM-IP-RD-MIB", "rdEntry")
zhoneIp, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneIp", "zhoneModules")
comIpIcmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 55))
comIpIcmp.setRevisions(('2000-09-11 16:25',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: comIpIcmp.setRevisionsDescriptions(('V01.00.00 - Initial Release',))
if mibBuilder.loadTexts: comIpIcmp.setLastUpdated('200009111648Z')
if mibBuilder.loadTexts: comIpIcmp.setOrganization('Zhone Technologies')
if mibBuilder.loadTexts: comIpIcmp.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com ')
if mibBuilder.loadTexts: comIpIcmp.setDescription('Zhone ICMP MIB Module. IP Software Minneapolis, MN')
icmp = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5))
if mibBuilder.loadTexts: icmp.setStatus('current')
if mibBuilder.loadTexts: icmp.setDescription('ICMP objects based on RFC 2011.')
zhoneIcmpTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1), )
if mibBuilder.loadTexts: zhoneIcmpTable.setStatus('current')
if mibBuilder.loadTexts: zhoneIcmpTable.setDescription('Zhone ICMP Table.')
zhoneIcmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1), )
rdEntry.registerAugmentions(("ZHONE-COM-IP-ICMP-MIB", "zhoneIcmpEntry"))
zhoneIcmpEntry.setIndexNames(*rdEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneIcmpEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneIcmpEntry.setDescription('Zhone ICMP Entry. This table augments the Routing Domain Table defined in comIpRD.mib.')
zhIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInMsgs.setReference('See RFC2011: icmp.icmpInMsgs')
if mibBuilder.loadTexts: zhIcmpInMsgs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInMsgs.setDescription('The total number of ICMP messages which the entity received. Note that this counter includes all those counted by icmpInErrors.')
zhIcmpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInErrors.setReference('See RFC2011: icmp.icmpInErrors')
if mibBuilder.loadTexts: zhIcmpInErrors.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInErrors.setDescription('The number of ICMP messages which the entity received but determined as having ICMP-specific errors (bad ICMP checksums, bad length, etc.).')
zhIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInDestUnreachs.setReference('See RFC2011: icmp.icmpInDestUnreachs')
if mibBuilder.loadTexts: zhIcmpInDestUnreachs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInDestUnreachs.setDescription('The number of ICMP Destination Unreachable messages received.')
zhIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInTimeExcds.setReference('See RFC2011: icmp.icmpInTimeExcds')
if mibBuilder.loadTexts: zhIcmpInTimeExcds.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInTimeExcds.setDescription('The number of ICMP Time Exceeded messages received.')
zhIcmpInParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInParmProbs.setReference('See RFC2011: icmp.icmpInParmProbs')
if mibBuilder.loadTexts: zhIcmpInParmProbs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInParmProbs.setDescription('The number of ICMP Parameter Problem messages received.')
zhIcmpInSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInSrcQuenchs.setReference('See RFC2011: icmp.icmpInSrcQuenchs')
if mibBuilder.loadTexts: zhIcmpInSrcQuenchs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInSrcQuenchs.setDescription('The number of ICMP Source Quench messages received.')
zhIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInRedirects.setReference('See RFC2011: icmp.icmpInRedirects')
if mibBuilder.loadTexts: zhIcmpInRedirects.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInRedirects.setDescription('The number of ICMP Redirect messages received.')
zhIcmpInEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInEchos.setReference('See RFC2011: icmp.icmpInEchos')
if mibBuilder.loadTexts: zhIcmpInEchos.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInEchos.setDescription('The number of ICMP Echo (request) messages received.')
zhIcmpInEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInEchoReps.setReference('See RFC2011: icmp.icmpInEchoReps')
if mibBuilder.loadTexts: zhIcmpInEchoReps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInEchoReps.setDescription('The number of ICMP Echo Reply messages received.')
zhIcmpInTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInTimestamps.setReference('See RFC2011: icmp.icmpInTimestamps')
if mibBuilder.loadTexts: zhIcmpInTimestamps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInTimestamps.setDescription('The number of ICMP Timestamp (request) messages received.')
zhIcmpInTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInTimestampReps.setReference('See RFC2011: icmp.icmpInTimestampReps')
if mibBuilder.loadTexts: zhIcmpInTimestampReps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInTimestampReps.setDescription('The number of ICMP Timestamp Reply messages received.')
zhIcmpInAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInAddrMasks.setReference('See RFC2011: icmp.icmpInAddrMasks')
if mibBuilder.loadTexts: zhIcmpInAddrMasks.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInAddrMasks.setDescription('The number of ICMP Address Mask Request messages received.')
zhIcmpInAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpInAddrMaskReps.setReference('See RFC2011: icmp.icmpInAddrMaskReps')
if mibBuilder.loadTexts: zhIcmpInAddrMaskReps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpInAddrMaskReps.setDescription('The number of ICMP Address Mask Reply messages received.')
zhIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutMsgs.setReference('See RFC2011: icmp.icmpOutMsgs')
if mibBuilder.loadTexts: zhIcmpOutMsgs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutMsgs.setDescription('The total number of ICMP messages which this entity attempted to send. Note that this counter includes all those counted by icmpOutErrors.')
zhIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutErrors.setReference('See RFC2011: icmp.icmpOutErrors')
if mibBuilder.loadTexts: zhIcmpOutErrors.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutErrors.setDescription("The number of ICMP messages which this entity did not send due to problems discovered within ICMP such as a lack of buffers. This value should not include errors discovered outside the ICMP layer such as the inability of IP to route the resultant datagram. In some implementations there may be no types of error which contribute to this counter's value.")
zhIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutDestUnreachs.setReference('See RFC2011: icmp.icmpOutDestUnreachs')
if mibBuilder.loadTexts: zhIcmpOutDestUnreachs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutDestUnreachs.setDescription('The number of ICMP Destination Unreachable messages sent.')
zhIcmpOutTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutTimeExcds.setReference('See RFC2011: icmp.icmpOutTimeExcds')
if mibBuilder.loadTexts: zhIcmpOutTimeExcds.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutTimeExcds.setDescription('The number of ICMP Time Exceeded messages sent.')
zhIcmpOutParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutParmProbs.setReference('See RFC2011: icmp.icmpOutParmProbs')
if mibBuilder.loadTexts: zhIcmpOutParmProbs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutParmProbs.setDescription('The number of ICMP Parameter Problem messages sent.')
zhIcmpOutSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutSrcQuenchs.setReference('See RFC2011: icmp.icmpOutSrcQuenchs')
if mibBuilder.loadTexts: zhIcmpOutSrcQuenchs.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutSrcQuenchs.setDescription('The number of ICMP Source Quench messages sent.')
zhIcmpOutRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutRedirects.setReference('See RFC2011: icmp.icmpOutRedirects')
if mibBuilder.loadTexts: zhIcmpOutRedirects.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutRedirects.setDescription('The number of ICMP Redirect messages sent. For a host, this object will always be zero, since hosts do not send redirects.')
zhIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutEchos.setReference('See RFC2011: icmp.icmpOutEchos')
if mibBuilder.loadTexts: zhIcmpOutEchos.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutEchos.setDescription('The number of ICMP Echo (request) messages sent.')
zhIcmpOutEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutEchoReps.setReference('See RFC2011: icmp.icmpOutEchoReps')
if mibBuilder.loadTexts: zhIcmpOutEchoReps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutEchoReps.setDescription('The number of ICMP Echo Reply messages sent.')
zhIcmpOutTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutTimestamps.setReference('See RFC2011: icmp.icmpOutTimestamps')
if mibBuilder.loadTexts: zhIcmpOutTimestamps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutTimestamps.setDescription('The number of ICMP Timestamp (request) messages sent.')
zhIcmpOutTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutTimestampReps.setReference('See RFC2011: icmp.icmpOutTimestampReps')
if mibBuilder.loadTexts: zhIcmpOutTimestampReps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutTimestampReps.setDescription('The number of ICMP Timestamp Reply messages sent.')
zhIcmpOutAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutAddrMasks.setReference('See RFC2011: icmp.icmpOutAddrMasks')
if mibBuilder.loadTexts: zhIcmpOutAddrMasks.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutAddrMasks.setDescription('The number of ICMP Address Mask Request messages sent.')
zhIcmpOutAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhIcmpOutAddrMaskReps.setReference('See RFC2011: icmp.icmpOutAddrMaskReps')
if mibBuilder.loadTexts: zhIcmpOutAddrMaskReps.setStatus('current')
if mibBuilder.loadTexts: zhIcmpOutAddrMaskReps.setDescription('The number of ICMP Address Mask Reply messages sent.')
mibBuilder.exportSymbols("ZHONE-COM-IP-ICMP-MIB", zhIcmpInRedirects=zhIcmpInRedirects, icmp=icmp, zhIcmpOutAddrMasks=zhIcmpOutAddrMasks, zhIcmpOutMsgs=zhIcmpOutMsgs, zhIcmpInMsgs=zhIcmpInMsgs, zhIcmpOutErrors=zhIcmpOutErrors, zhIcmpInEchoReps=zhIcmpInEchoReps, zhIcmpInEchos=zhIcmpInEchos, zhIcmpOutSrcQuenchs=zhIcmpOutSrcQuenchs, zhIcmpOutAddrMaskReps=zhIcmpOutAddrMaskReps, zhIcmpInAddrMaskReps=zhIcmpInAddrMaskReps, zhIcmpInTimeExcds=zhIcmpInTimeExcds, zhIcmpOutEchos=zhIcmpOutEchos, zhIcmpInParmProbs=zhIcmpInParmProbs, zhoneIcmpTable=zhoneIcmpTable, zhIcmpInErrors=zhIcmpInErrors, zhIcmpOutEchoReps=zhIcmpOutEchoReps, zhIcmpOutTimeExcds=zhIcmpOutTimeExcds, zhIcmpOutTimestampReps=zhIcmpOutTimestampReps, PYSNMP_MODULE_ID=comIpIcmp, zhIcmpOutTimestamps=zhIcmpOutTimestamps, comIpIcmp=comIpIcmp, zhIcmpInDestUnreachs=zhIcmpInDestUnreachs, zhIcmpOutDestUnreachs=zhIcmpOutDestUnreachs, zhIcmpInTimestampReps=zhIcmpInTimestampReps, zhoneIcmpEntry=zhoneIcmpEntry, zhIcmpInSrcQuenchs=zhIcmpInSrcQuenchs, zhIcmpInAddrMasks=zhIcmpInAddrMasks, zhIcmpInTimestamps=zhIcmpInTimestamps, zhIcmpOutParmProbs=zhIcmpOutParmProbs, zhIcmpOutRedirects=zhIcmpOutRedirects)
