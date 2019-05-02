#
# PySNMP MIB module ASCEND-ATMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-ATMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
DisplayString, atmpGroup = mibBuilder.importSymbols("ASCEND-MIB", "DisplayString", "atmpGroup")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, NotificationType, iso, Integer32, Bits, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "NotificationType", "iso", "Integer32", "Bits", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmpAgentMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("atmp-disabled", 1), ("home-agent", 2), ("foreign-agent", 3), ("both-agent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentMode.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentMode.setDescription('The type of ATMP Agent.')
atmpAgentType = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ha-router", 1), ("ha-gateway", 2), ("ha-notapp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentType.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentType.setDescription('The type of ATMP HA Agent. ha-router means the HA will route the tunneled data to other networks. ha-gateway means the HA delivers tunneled data to other networks without routing anything. A ha-notapp will be returned for FA and if ATMP is disabled.')
atmpAgentUDPPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentUDPPort.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentUDPPort.setDescription('UDP port number to be used for ATMP.')
atmpAgentGreMtu = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentGreMtu.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentGreMtu.setDescription('The maximum IP packet size that can be transmitted to a peer agent without performing fragmentation. The value 0 means this feature is disabled.')
atmpAgentForceFragmentation = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentForceFragmentation.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentForceFragmentation.setDescription('To force fragmentation of large IP frames before they are sent to the peer agent even if the packet has the DF bit set. NOTE: this behavior is not standard and prevents MTU discovery mechanisms. This works in conjunction with atmpAgentGreMtu.')
atmpAgentHAIdleLimit = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentHAIdleLimit.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentHAIdleLimit.setDescription('Time in minutes that the HA will allow a tunnel to have no traffic before tearing it down. The value 0 means this option is disabled.')
atmpLastErrorGenerated = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("no-error", 1), ("fa-auth-failed", 2), ("ha-atmp-disabled", 3), ("too-many-tunnel", 4), ("err-parameter", 5), ("bad-tunnel", 6), ("err-timeout", 7), ("hn-unreachable", 8), ("dns-failed", 9), ("err-general", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpLastErrorGenerated.setStatus('mandatory')
if mibBuilder.loadTexts: atmpLastErrorGenerated.setDescription('This is the last error at the Agent level or Tunnel creation that was generated by the Agent. To clear the field and atmpAgentSentErrorTo do a set with the value no-error(1)')
atmpAgentSentErrorTo = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentSentErrorTo.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentSentErrorTo.setDescription('The IP Address of the agent that the generated was sent to. Clearing atmpLastErrorGenerated also clears this field.')
atmpLastErrorRecv = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("no-error", 1), ("fa-auth-failed", 2), ("ha-atmp-disabled", 3), ("too-many-tunnel", 4), ("err-parameter", 5), ("bad-tunnel", 6), ("err-timeout", 7), ("hn-unreachable", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpLastErrorRecv.setStatus('mandatory')
if mibBuilder.loadTexts: atmpLastErrorRecv.setDescription('This is the last error at the Agent level or Tunnel creation that was received from the Peer Agent. To clear the field and atmpAgentRecvErrorFrom do a set with the value no-error(1)')
atmpAgentRecvErrorFrom = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentRecvErrorFrom.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentRecvErrorFrom.setDescription('The IP Address of the agent that the last error received was from. Clearing atmpLastErrorRecv also clears this field.')
atmpEnableAtmpTraps = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpEnableAtmpTraps.setStatus('mandatory')
if mibBuilder.loadTexts: atmpEnableAtmpTraps.setDescription('Enable the atmp traps.')
atmpAgentNumberFATunnels = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentNumberFATunnels.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentNumberFATunnels.setDescription('The number of FA tunnels.')
atmpAgentNumberHATunnels = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentNumberHATunnels.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentNumberHATunnels.setDescription('The number of HA tunnels.')
atmpAgentNumberLocalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentNumberLocalTunnels.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentNumberLocalTunnels.setDescription('The number of Local client mode tunnels.')
atmpAgentTunnelHighWater = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentTunnelHighWater.setStatus('mandatory')
if mibBuilder.loadTexts: atmpAgentTunnelHighWater.setDescription('The high water mark on created ATMP tunnels.')
atmpTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 529, 24, 16), )
if mibBuilder.loadTexts: atmpTunnelTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmpTunnelTable.setDescription('A list of ATMP tunnel entries.')
atmpTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 24, 16, 1), ).setIndexNames((0, "ASCEND-ATMP-MIB", "atmpTunnelIndex"))
if mibBuilder.loadTexts: atmpTunnelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmpTunnelEntry.setDescription('A ATMP tunnel entry.')
atmpTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmpTunnelIndex.setDescription('A unique index assigned to this tunnel.')
atmpTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelId.setStatus('mandatory')
if mibBuilder.loadTexts: atmpTunnelId.setDescription('The tunnel ID assigned to this tunnel. This number is assigned by the HA. NOTE: this number does *not* uniquely identify a tunnel.')
atmpHAIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpHAIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmpHAIpAddress.setDescription("The IP Address of this tunnel's HA.")
atmpFAIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFAIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmpFAIpAddress.setDescription("The IP Address of this tunnel's FA.")
atmpTunneledProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ip", 1), ("ipx", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunneledProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: atmpTunneledProtocol.setDescription("This value indicates the protocol(s) that the tunnel supports. The value is a sum. The sum initially takes the value zero. Then for each protocol that is supported, the value of the protocol is or'ed to the sum. Example: 3 means ip and ipx.")
atmpTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ha", 1), ("fa", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelType.setStatus('mandatory')
if mibBuilder.loadTexts: atmpTunnelType.setDescription('The type of tunnel this is.')
atmpTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("registering", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelState.setStatus('mandatory')
if mibBuilder.loadTexts: atmpTunnelState.setDescription('These are the states the tunnel can be in. ')
atmpMnIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmpMnIpAddress.setDescription('The IP Address of the Mobile Node.')
atmpMnNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnNetmask.setStatus('mandatory')
if mibBuilder.loadTexts: atmpMnNetmask.setDescription('The netmask of the Mobile Node.')
atmpMnIpxNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnIpxNetAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmpMnIpxNetAddress.setDescription('The IPX network address of the Mobile Node.')
atmpMnIpxNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnIpxNodeAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmpMnIpxNodeAddress.setDescription('The IPX node address of the Mobile Node.')
atmpHNProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpHNProfileName.setStatus('mandatory')
if mibBuilder.loadTexts: atmpHNProfileName.setDescription('The name of the home network profile which will be used to forward all packets received by the HA. This may be NULL if the HA is in router mode.')
atmpHNMaxTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpHNMaxTunnels.setStatus('mandatory')
if mibBuilder.loadTexts: atmpHNMaxTunnels.setDescription('The maximum number of tunnels allowed to this HN.')
atmpFAPrimaryHAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFAPrimaryHAAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmpFAPrimaryHAAddress.setDescription('The Address of the Primary HA. This is known on the FA and will be NULL if the tunnel is on the HA.')
atmpFASecondaryHAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFASecondaryHAAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmpFASecondaryHAAddress.setDescription('The Address of the secondary HA. This is known only on the FA and will be NULL if the tunnel is on the HA.')
atmpFASsnStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFASsnStatusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmpFASsnStatusIndex.setDescription('The session status entry index. This is used to tie in the tunnel with a mobile node. It is the same as ssnStatusIndex. This is only known on the FA and will be 0 if the tunnel is on the HA.')
atmpFAUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFAUserName.setStatus('mandatory')
if mibBuilder.loadTexts: atmpFAUserName.setDescription('The name of the mobile node. This is only known on the FA and will be NULL if the tunnel is on the HA.')
atmpInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpInPkts.setStatus('mandatory')
if mibBuilder.loadTexts: atmpInPkts.setDescription('The number of packets received on this tunnel from the peer Agent. Not valid for tunnels in local client mode. ')
atmpInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: atmpInOctets.setDescription('The number of octets received on this tunnel from the peer Agent. Not valid for tunnels in local client mode. ')
atmpInErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpInErrPkts.setStatus('mandatory')
if mibBuilder.loadTexts: atmpInErrPkts.setDescription('The number of packets received on this tunnel from the peer Agent that were dropped. Not valid for tunnels in local client mode. ')
atmpOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpOutPkts.setStatus('mandatory')
if mibBuilder.loadTexts: atmpOutPkts.setDescription('The number of packets sent on this tunnel to the peer Agent. Not valid for tunnels in local client mode. ')
atmpOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: atmpOutOctets.setDescription('The number of octets sent on this tunnel to the peer Agent. Not valid for tunnels in local client mode. ')
atmpOutErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpOutErrPkts.setStatus('mandatory')
if mibBuilder.loadTexts: atmpOutErrPkts.setDescription('The number of packets dropped on this tunnel before sending to peer Agent. Not valid for tunnels in local client mode. ')
atmpPktsForcedToFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpPktsForcedToFragment.setStatus('mandatory')
if mibBuilder.loadTexts: atmpPktsForcedToFragment.setDescription('The number of packets forced to pre-fragment despite the DF bit. Not valid for tunnels in local client mode. ')
atmpPktsFailedFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpPktsFailedFragment.setStatus('mandatory')
if mibBuilder.loadTexts: atmpPktsFailedFragment.setDescription('The number of packets that required to be fragmented but were dropped because atmpAgentForceFragemtnation was disable and the DF bit was set. Not valid for tunnels in local client mode.')
mibBuilder.exportSymbols("ASCEND-ATMP-MIB", atmpAgentUDPPort=atmpAgentUDPPort, atmpEnableAtmpTraps=atmpEnableAtmpTraps, atmpMnIpxNetAddress=atmpMnIpxNetAddress, atmpFASsnStatusIndex=atmpFASsnStatusIndex, atmpLastErrorGenerated=atmpLastErrorGenerated, atmpHAIpAddress=atmpHAIpAddress, atmpLastErrorRecv=atmpLastErrorRecv, atmpMnIpAddress=atmpMnIpAddress, atmpInOctets=atmpInOctets, atmpTunneledProtocol=atmpTunneledProtocol, atmpTunnelState=atmpTunnelState, atmpOutOctets=atmpOutOctets, atmpPktsForcedToFragment=atmpPktsForcedToFragment, atmpAgentNumberLocalTunnels=atmpAgentNumberLocalTunnels, atmpHNProfileName=atmpHNProfileName, atmpAgentHAIdleLimit=atmpAgentHAIdleLimit, atmpAgentForceFragmentation=atmpAgentForceFragmentation, atmpTunnelTable=atmpTunnelTable, atmpFASecondaryHAAddress=atmpFASecondaryHAAddress, atmpAgentMode=atmpAgentMode, atmpAgentTunnelHighWater=atmpAgentTunnelHighWater, atmpMnNetmask=atmpMnNetmask, atmpMnIpxNodeAddress=atmpMnIpxNodeAddress, atmpFAPrimaryHAAddress=atmpFAPrimaryHAAddress, atmpInPkts=atmpInPkts, atmpAgentGreMtu=atmpAgentGreMtu, atmpInErrPkts=atmpInErrPkts, atmpAgentNumberFATunnels=atmpAgentNumberFATunnels, atmpTunnelId=atmpTunnelId, atmpAgentRecvErrorFrom=atmpAgentRecvErrorFrom, atmpHNMaxTunnels=atmpHNMaxTunnels, atmpPktsFailedFragment=atmpPktsFailedFragment, atmpAgentSentErrorTo=atmpAgentSentErrorTo, atmpOutErrPkts=atmpOutErrPkts, atmpAgentNumberHATunnels=atmpAgentNumberHATunnels, atmpOutPkts=atmpOutPkts, atmpTunnelType=atmpTunnelType, atmpFAIpAddress=atmpFAIpAddress, atmpFAUserName=atmpFAUserName, atmpAgentType=atmpAgentType, atmpTunnelEntry=atmpTunnelEntry, atmpTunnelIndex=atmpTunnelIndex)
