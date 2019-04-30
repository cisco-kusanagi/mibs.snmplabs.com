#
# PySNMP MIB module HP-SN-IP-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-IP-ACL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
snIp, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "snIp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, iso, Counter32, Integer32, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "iso", "Counter32", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

class RtrStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class SnRowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4))

class Action(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("deny", 0), ("permit", 1))

class TruthVal(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("false", 0), ("true", 1))

class AclNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 199)

class Operator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 7))
    namedValues = NamedValues(("eq", 0), ("neq", 1), ("lt", 2), ("gt", 3), ("range", 4), ("undefined", 7))

class IpProtocol(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PrecedenceValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(5, 3, 4, 2, 6, 7, 1, 0, 8))
    namedValues = NamedValues(("critical", 5), ("flash", 3), ("flashoverride", 4), ("immediate", 2), ("internet", 6), ("network", 7), ("priority", 1), ("routine", 0), ("undefined", 8))

class TosValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("normal", 0), ("minMonetaryCost", 1), ("maxReliability", 2), ("tosValue3", 3), ("maxThroughput", 4), ("tosValue5", 5), ("tosValue6", 6), ("tosValue7", 7), ("minDelay", 8), ("tosValue9", 9), ("tosValue10", 10), ("tosValue11", 11), ("tosValue12", 12), ("tosValue13", 13), ("tosValue14", 14), ("tosValue15", 15), ("undefined", 16))

class Direction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inbound", 0), ("outbound", 1))

snAgAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15))
snAgAclGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 1))
snAgAclGblCurRowIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclGblCurRowIndex.setStatus('mandatory')
snAgAclTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2), )
if mibBuilder.loadTexts: snAgAclTable.setStatus('mandatory')
snAgAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1), ).setIndexNames((0, "HP-SN-IP-ACL-MIB", "snAgAclIndex"))
if mibBuilder.loadTexts: snAgAclEntry.setStatus('mandatory')
snAgAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclIndex.setStatus('mandatory')
snAgAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 2), AclNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNumber.setStatus('mandatory')
snAgAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclName.setStatus('mandatory')
snAgAclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclAction.setStatus('mandatory')
snAgAclProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 5), IpProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclProtocol.setStatus('mandatory')
snAgAclSourceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceIp.setStatus('mandatory')
snAgAclSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceMask.setStatus('mandatory')
snAgAclSourceOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 8), Operator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperator.setStatus('mandatory')
snAgAclSourceOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperand1.setStatus('mandatory')
snAgAclSourceOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperand2.setStatus('mandatory')
snAgAclDestinationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationIp.setStatus('mandatory')
snAgAclDestinationMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationMask.setStatus('mandatory')
snAgAclDestinationOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 13), Operator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperator.setStatus('mandatory')
snAgAclDestinationOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperand1.setStatus('mandatory')
snAgAclDestinationOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperand2.setStatus('mandatory')
snAgAclPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 16), PrecedenceValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPrecedence.setStatus('mandatory')
snAgAclTos = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 17), TosValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclTos.setStatus('mandatory')
snAgAclEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 18), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclEstablished.setStatus('mandatory')
snAgAclLogOption = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 19), TruthVal()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclLogOption.setStatus('mandatory')
snAgAclStandardFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 20), TruthVal()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclStandardFlag.setStatus('mandatory')
snAgAclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 21), SnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclRowStatus.setStatus('mandatory')
snAgAclFlowCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclFlowCounter.setStatus('mandatory')
snAgAclPacketCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPacketCounter.setStatus('mandatory')
snAgAclComments = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 24), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclComments.setStatus('mandatory')
snAgAclIpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclIpPriority.setStatus('mandatory')
snAgAclPriorityForce = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPriorityForce.setStatus('mandatory')
snAgAclPriorityMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPriorityMapping.setStatus('mandatory')
snAgAclDscpMarking = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDscpMarking.setStatus('mandatory')
snAgAclDscpMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDscpMapping.setStatus('mandatory')
snAgAclBindToPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3), )
if mibBuilder.loadTexts: snAgAclBindToPortTable.setStatus('mandatory')
snAgAclBindToPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1), ).setIndexNames((0, "HP-SN-IP-ACL-MIB", "snAgAclPortNum"), (0, "HP-SN-IP-ACL-MIB", "snAgAclPortBindDirection"))
if mibBuilder.loadTexts: snAgAclBindToPortEntry.setStatus('mandatory')
snAgAclPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPortNum.setStatus('mandatory')
snAgAclPortBindDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 2), Direction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPortBindDirection.setStatus('mandatory')
snAgAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNum.setStatus('mandatory')
snAgAclNameString = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNameString.setStatus('mandatory')
snAgBindPortListInVirtualInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgBindPortListInVirtualInterface.setStatus('mandatory')
snAgAclPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 6), SnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPortRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("HP-SN-IP-ACL-MIB", snAgAclSourceIp=snAgAclSourceIp, snAgAclGlobal=snAgAclGlobal, PrecedenceValue=PrecedenceValue, snAgAclDestinationOperand2=snAgAclDestinationOperand2, snAgAcl=snAgAcl, Action=Action, snAgAclTos=snAgAclTos, snAgAclFlowCounter=snAgAclFlowCounter, DisplayString=DisplayString, snAgAclSourceMask=snAgAclSourceMask, snAgAclPriorityMapping=snAgAclPriorityMapping, Operator=Operator, snAgAclName=snAgAclName, snAgAclEstablished=snAgAclEstablished, snAgAclDestinationOperator=snAgAclDestinationOperator, snAgAclStandardFlag=snAgAclStandardFlag, snAgAclDestinationOperand1=snAgAclDestinationOperand1, snAgAclPortNum=snAgAclPortNum, snAgBindPortListInVirtualInterface=snAgBindPortListInVirtualInterface, snAgAclDestinationIp=snAgAclDestinationIp, snAgAclDscpMapping=snAgAclDscpMapping, snAgAclGblCurRowIndex=snAgAclGblCurRowIndex, TruthVal=TruthVal, snAgAclIpPriority=snAgAclIpPriority, Direction=Direction, snAgAclNameString=snAgAclNameString, snAgAclLogOption=snAgAclLogOption, snAgAclAction=snAgAclAction, RtrStatus=RtrStatus, snAgAclDestinationMask=snAgAclDestinationMask, snAgAclIndex=snAgAclIndex, snAgAclPrecedence=snAgAclPrecedence, snAgAclProtocol=snAgAclProtocol, TosValue=TosValue, snAgAclSourceOperator=snAgAclSourceOperator, snAgAclBindToPortEntry=snAgAclBindToPortEntry, snAgAclRowStatus=snAgAclRowStatus, IpProtocol=IpProtocol, SnRowStatus=SnRowStatus, snAgAclNum=snAgAclNum, snAgAclPortBindDirection=snAgAclPortBindDirection, snAgAclComments=snAgAclComments, snAgAclBindToPortTable=snAgAclBindToPortTable, snAgAclNumber=snAgAclNumber, snAgAclPacketCounter=snAgAclPacketCounter, snAgAclSourceOperand2=snAgAclSourceOperand2, snAgAclPortRowStatus=snAgAclPortRowStatus, snAgAclPriorityForce=snAgAclPriorityForce, snAgAclEntry=snAgAclEntry, snAgAclDscpMarking=snAgAclDscpMarking, snAgAclTable=snAgAclTable, AclNumber=AclNumber, snAgAclSourceOperand1=snAgAclSourceOperand1)
