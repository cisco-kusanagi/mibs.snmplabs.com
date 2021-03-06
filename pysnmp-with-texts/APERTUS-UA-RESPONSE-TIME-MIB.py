#
# PySNMP MIB module APERTUS-UA-RESPONSE-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APERTUS-UA-RESPONSE-TIME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, mib_2, Gauge32, iso, ObjectIdentity, Counter64, Unsigned32, IpAddress, MibIdentifier, Integer32, NotificationType, TimeTicks, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "mib-2", "Gauge32", "iso", "ObjectIdentity", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "TimeTicks", "Counter32", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
apertus = MibIdentifier((1, 3, 6, 1, 4, 1, 543))
isg = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3))
aperua = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3))
aperresponsetime = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 5))
aperResponseTimeMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1))
aperResponseTimeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1))
aperResponseTimeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 1))
aperResponseTimeDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2))
aperResponseTimeNode = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3))
aperResponseTimeConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ready", 1), ("loading", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeConfigStatus.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeConfigStatus.setDescription('Status of Universal Access server')
aperResponseTimeConfigUpTime = MibScalar((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeConfigUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeConfigUpTime.setDescription('This value represents the time elapsed since the server was started in 1/100nths of a second.')
aperResponseTimeDomainTable = MibTable((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1), )
if mibBuilder.loadTexts: aperResponseTimeDomainTable.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeDomainTable.setDescription('Domain information broken down domain name.')
aperResponseTimeDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1), ).setIndexNames((0, "APERTUS-UA-RESPONSE-TIME-MIB", "aperResponseTimeDomainName"))
if mibBuilder.loadTexts: aperResponseTimeDomainEntry.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeDomainEntry.setDescription('This table contains information on each of the load balance domains under its control.')
aperResponseTimeDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeDomainName.setDescription('The zone name for this load-balance domain.')
aperResponseTimeDomainUpServers = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeDomainUpServers.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeDomainUpServers.setDescription('The number of servers that are up at this time.')
aperResponseTimeDomainDownServers = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeDomainDownServers.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeDomainDownServers.setDescription('The number of servers in list that are marked as down at this time.')
aperResponseTimeDomainCompareMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absolute", 1), ("percentage", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeDomainCompareMethod.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeDomainCompareMethod.setDescription('How the ...NodeWindow field is interpreted. If the compare method is absolute, the values are compared by absolute adjustments to the response time. (EG, a 10ms response time with a window of 40 in a absolute domain will have an effective compare time of 50ms). A percentage domain indicates that the values are offset by the given percentage. (EG, a 20ms responsetime with a window of 400 will have am effective compare time of 80ms). Note that to leave a value unadjusted, the window needs to be 100.')
aperResponseTimeNodeTable = MibTable((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1), )
if mibBuilder.loadTexts: aperResponseTimeNodeTable.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeTable.setDescription('Node information broken down domain name and IP address')
aperResponseTimeNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1), ).setIndexNames((0, "APERTUS-UA-RESPONSE-TIME-MIB", "aperResponseTimeNodeName"), (0, "APERTUS-UA-RESPONSE-TIME-MIB", "aperResponseTimeNodeIP"))
if mibBuilder.loadTexts: aperResponseTimeNodeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeEntry.setDescription('This table contains information on each of the machines in the different laod balance zones.')
aperResponseTimeNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeNodeName.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeName.setDescription('The zone name for this Node.')
aperResponseTimeNodeIP = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeNodeIP.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeIP.setDescription('The IP address of the NODE.')
aperResponseTimeNodeWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeNodeWindow.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeWindow.setDescription('The window offset for this node vs other nodes within the same pool level. Please see the description for the domain field ...CompareMethod for more information on this fields usage.')
aperResponseTimeNodePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeNodePoolIndex.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodePoolIndex.setDescription('This value is the pool index. When all nodes with a lower index are down, the items with next highest pool index are considered for responseTime usage.')
aperResponseTimeNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notqueried", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeNodeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeStatus.setDescription('Indicates the status of the node. Up(1) shows that the node is up and is being considered for use. Down(2) indicates that the last query to the NODE image resulted in a down marker for the node. Admindown(3) indicates that an administrator took the node offline manually (from the UA server end). Notqueried(4) is used to indicate that a node has never been queried.')
aperResponseTimeNodeResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeNodeResponseTime.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeResponseTime.setDescription('Response time in MS of last node access. A value of 0 is returned if NodeStatus is not ready(1) or if the node has never been queried')
aperResponseTimeNodeAdjustedCompareValue = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperResponseTimeNodeAdjustedCompareValue.setStatus('mandatory')
if mibBuilder.loadTexts: aperResponseTimeNodeAdjustedCompareValue.setDescription('Response time as adjusted by the window value.')
mibBuilder.exportSymbols("APERTUS-UA-RESPONSE-TIME-MIB", aperResponseTimeDomainDownServers=aperResponseTimeDomainDownServers, aperResponseTimeDomainEntry=aperResponseTimeDomainEntry, mgmt=mgmt, aperResponseTimeNodeEntry=aperResponseTimeNodeEntry, aperResponseTimeConfigStatus=aperResponseTimeConfigStatus, isg=isg, aperResponseTimeConfig=aperResponseTimeConfig, experimental=experimental, enterprises=enterprises, aperResponseTimeDomainCompareMethod=aperResponseTimeDomainCompareMethod, aperResponseTimeDomainTable=aperResponseTimeDomainTable, aperResponseTimeConfigUpTime=aperResponseTimeConfigUpTime, aperResponseTimeNodeTable=aperResponseTimeNodeTable, aperResponseTimeDomainUpServers=aperResponseTimeDomainUpServers, aperResponseTimeNodeIP=aperResponseTimeNodeIP, aperResponseTimeNodeResponseTime=aperResponseTimeNodeResponseTime, private=private, aperua=aperua, aperResponseTimeDomainName=aperResponseTimeDomainName, aperResponseTimeNodeAdjustedCompareValue=aperResponseTimeNodeAdjustedCompareValue, directory=directory, aperResponseTimeNode=aperResponseTimeNode, aperResponseTimeNodePoolIndex=aperResponseTimeNodePoolIndex, aperResponseTimeMIBObjects=aperResponseTimeMIBObjects, aperResponseTimeNodeWindow=aperResponseTimeNodeWindow, aperResponseTimeNodeName=aperResponseTimeNodeName, aperResponseTimeNodeStatus=aperResponseTimeNodeStatus, internet=internet, aperresponsetime=aperresponsetime, apertus=apertus, aperResponseTimeMIB=aperResponseTimeMIB, aperResponseTimeDomain=aperResponseTimeDomain)
