#
# PySNMP MIB module FOUNDRY-CAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-CAR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, iso, Bits, Counter64, MibIdentifier, Integer32, Gauge32, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "iso", "Bits", "Counter64", "MibIdentifier", "Integer32", "Gauge32", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snCAR = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16))
snCAR.setRevisions(('2010-06-02 00:00', '2009-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snCAR.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'convert from SMIv1 to SMIv2',))
if mibBuilder.loadTexts: snCAR.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snCAR.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: snCAR.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: snCAR.setDescription("Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
snPortCARs = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1))
class PacketSource(TextualConvention, Integer32):
    description = ' '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("input", 0), ("output", 1))

class RateLimitType(TextualConvention, Integer32):
    description = ' '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 2, 1))
    namedValues = NamedValues(("all", 3), ("quickAcc", 2), ("standardAcc", 1))

class RateLimitAction(TextualConvention, Integer32):
    description = ' '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("continue", 1), ("drop", 2), ("precedCont", 3), ("precedXmit", 4), ("xmit", 5))

snPortCARTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1), )
if mibBuilder.loadTexts: snPortCARTable.setStatus('current')
if mibBuilder.loadTexts: snPortCARTable.setDescription('A table of rate limit configuration entries. Rate Limit is a method of traffic control. It allows a set of rate limits to be configured and applied to packets flowing into/out of an interface to regulate network traffic.')
snPortCAREntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1), ).setIndexNames((0, "FOUNDRY-CAR-MIB", "snPortCARifIndex"), (0, "FOUNDRY-CAR-MIB", "snPortCARDirection"), (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"))
if mibBuilder.loadTexts: snPortCAREntry.setStatus('current')
if mibBuilder.loadTexts: snPortCAREntry.setDescription('A collection of rate-limit configuration objects on this interface.')
snPortCARifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARifIndex.setStatus('current')
if mibBuilder.loadTexts: snPortCARifIndex.setDescription('The ifIndex value for this rate limit entry.')
snPortCARDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 2), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARDirection.setStatus('current')
if mibBuilder.loadTexts: snPortCARDirection.setDescription('The input or output transmission direction for the Rate Limit object. input (0), --for inbound traffic output(1) --for outbound traffic ')
snPortCARRowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARRowIndex.setStatus('current')
if mibBuilder.loadTexts: snPortCARRowIndex.setDescription('The table index for rate limit objects. It increases as the rate limit entries are added. Skips the number when a row is deleted.')
snPortCARType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 4), RateLimitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARType.setStatus('current')
if mibBuilder.loadTexts: snPortCARType.setDescription('The type of traffic rate-limited against.')
snPortCARAccIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARAccIdx.setStatus('current')
if mibBuilder.loadTexts: snPortCARAccIdx.setDescription('The index to the access list if RateLimitType is either quickAcc or standardAcc.')
snPortCARRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARRate.setStatus('current')
if mibBuilder.loadTexts: snPortCARRate.setDescription('The comitted access rate. This determines the long term average transmission rate. Traffic that falls under this rate always conforms. This is average rate in bits per second.')
snPortCARLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARLimit.setStatus('current')
if mibBuilder.loadTexts: snPortCARLimit.setDescription('This is the normal burst size that determines how large traffic bursts can be before some traffic exceeds the rate limit. This specifies the number of bytes that are guaranteed to be transported by the network at the average rate under normal conditions during committed time interval. This normal burst size is in bytes.')
snPortCARExtLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARExtLimit.setStatus('current')
if mibBuilder.loadTexts: snPortCARExtLimit.setDescription('This is the extended burst limit that determines how large traffic bursts can be before all the traffic exceeds the rate limit. This burst size is in bytes.')
snPortCARConformAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 9), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARConformAction.setStatus('current')
if mibBuilder.loadTexts: snPortCARConformAction.setDescription('Action to be taken when the traffic is within the Rate Limit. drop drop the packet. xmit transmit the packet. continue continue to evaluate to the subsequent rate limits. precedXmit rewrite the IP precedence and transmit the packet. precedCont rewrite the IP precedence and allow it evaluated by subsequent rate limits.')
snPortCARExceedAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 10), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARExceedAction.setStatus('current')
if mibBuilder.loadTexts: snPortCARExceedAction.setDescription('Action to be taken when the traffic exceeds the Rate Limit.drop drop the packet. xmit transmit the packet. continue continue to evaluate to the subsequent rate limits. precedXmit rewrite the IP precedence and transmit the packet. precedCont rewrite the IP precedence and allow it evaluated by subsequent rate limits.')
snPortCARStatSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatSwitchedPkts.setStatus('current')
if mibBuilder.loadTexts: snPortCARStatSwitchedPkts.setDescription('The counter of packets permitted by this rate limit.')
snPortCARStatSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatSwitchedBytes.setStatus('current')
if mibBuilder.loadTexts: snPortCARStatSwitchedBytes.setDescription('The counter of bytes permitted by this interface.')
snPortCARStatFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatFilteredPkts.setStatus('current')
if mibBuilder.loadTexts: snPortCARStatFilteredPkts.setDescription('The counter of packets which exceeded this rate limit.')
snPortCARStatFilteredBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatFilteredBytes.setStatus('current')
if mibBuilder.loadTexts: snPortCARStatFilteredBytes.setDescription('The counter of bytes which exceeded this rate limit.')
snPortCARStatCurBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatCurBurst.setStatus('current')
if mibBuilder.loadTexts: snPortCARStatCurBurst.setDescription('The current received burst size.')
agRateLimitCounterTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2), )
if mibBuilder.loadTexts: agRateLimitCounterTable.setStatus('current')
if mibBuilder.loadTexts: agRateLimitCounterTable.setDescription('A table of rate limit counter entries.')
agRateLimitCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"))
if mibBuilder.loadTexts: agRateLimitCounterEntry.setStatus('current')
if mibBuilder.loadTexts: agRateLimitCounterEntry.setDescription('A collection of rate-limit counter objects on a interface, direction and configuration row index within that interface.')
agRateLimitCounterFwdedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterFwdedOctets.setStatus('current')
if mibBuilder.loadTexts: agRateLimitCounterFwdedOctets.setDescription('The forwarded octet count for this rate limit entry.')
agRateLimitCounterDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterDroppedOctets.setStatus('current')
if mibBuilder.loadTexts: agRateLimitCounterDroppedOctets.setDescription('The dropped octet count for this rate limit entry.')
agRateLimitCounterReMarkedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterReMarkedOctets.setStatus('current')
if mibBuilder.loadTexts: agRateLimitCounterReMarkedOctets.setDescription('The remarked octet count for this rate limit entry.')
agRateLimitCounterTotalOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterTotalOctets.setStatus('current')
if mibBuilder.loadTexts: agRateLimitCounterTotalOctets.setDescription('The total octet count for this rate limit entry.')
mibBuilder.exportSymbols("FOUNDRY-CAR-MIB", snPortCARStatFilteredBytes=snPortCARStatFilteredBytes, RateLimitType=RateLimitType, snPortCARRowIndex=snPortCARRowIndex, snPortCARStatCurBurst=snPortCARStatCurBurst, snPortCARExtLimit=snPortCARExtLimit, snPortCARStatSwitchedPkts=snPortCARStatSwitchedPkts, snPortCARifIndex=snPortCARifIndex, agRateLimitCounterReMarkedOctets=agRateLimitCounterReMarkedOctets, snPortCARDirection=snPortCARDirection, agRateLimitCounterFwdedOctets=agRateLimitCounterFwdedOctets, snPortCARRate=snPortCARRate, snPortCARExceedAction=snPortCARExceedAction, snPortCARConformAction=snPortCARConformAction, snPortCARTable=snPortCARTable, snPortCARType=snPortCARType, snPortCARStatFilteredPkts=snPortCARStatFilteredPkts, PacketSource=PacketSource, snPortCARLimit=snPortCARLimit, agRateLimitCounterTable=agRateLimitCounterTable, snCAR=snCAR, PYSNMP_MODULE_ID=snCAR, snPortCARs=snPortCARs, agRateLimitCounterDroppedOctets=agRateLimitCounterDroppedOctets, RateLimitAction=RateLimitAction, snPortCARStatSwitchedBytes=snPortCARStatSwitchedBytes, snPortCARAccIdx=snPortCARAccIdx, snPortCAREntry=snPortCAREntry, agRateLimitCounterTotalOctets=agRateLimitCounterTotalOctets, agRateLimitCounterEntry=agRateLimitCounterEntry)
