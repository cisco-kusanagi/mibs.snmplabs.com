#
# PySNMP MIB module ATM-POLICY-CONSTRAINT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-POLICY-CONSTRAINT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, ModuleIdentity, iso, TimeTicks, enterprises, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, IpAddress, Bits, Counter32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "iso", "TimeTicks", "enterprises", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "IpAddress", "Bits", "Counter32", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
atmPolicyConstraintMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1))
atmPolicyConstraintMIB.setRevisions(('2003-07-08 00:00',))
if mibBuilder.loadTexts: atmPolicyConstraintMIB.setLastUpdated('200307080000Z')
if mibBuilder.loadTexts: atmPolicyConstraintMIB.setOrganization('The ATM Forum.')
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmForumNetworkManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5))
atmfSignalling = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9))
atmfPolicyConstraint = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5))
policyConstraintMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1))
class NetworkEntityNetworkServiceCategory(TextualConvention, Integer32):
    reference = 'ATMF Policy Routing Version 1.0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65536)

class ResourcePartitionNetworkServiceCategory(TextualConvention, Integer32):
    reference = 'ATMF Policy Routing Version 1.0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PolicyConstraintIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PolicyConstraintPolicyIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 6)

class PolicyIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PolicyOperator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("requires", 1), ("mustAvoid", 2))

policyConstraintBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1))
policyConstraintMaximum = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyConstraintMaximum.setStatus('current')
policyMaximum = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyMaximum.setStatus('current')
policyNeNSCListMaximum = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyNeNSCListMaximum.setStatus('current')
policyRpNSCListMaximum = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyRpNSCListMaximum.setStatus('current')
policyConstraintGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2))
policyNextPolicyConstraintIndex = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 1), PolicyConstraintIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyNextPolicyConstraintIndex.setStatus('current')
policyConstraintTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2), )
if mibBuilder.loadTexts: policyConstraintTable.setStatus('current')
policyConstraintEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1), ).setIndexNames((0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintIndex"), (0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintPolicyIndex"))
if mibBuilder.loadTexts: policyConstraintEntry.setStatus('current')
policyConstraintIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 1), PolicyConstraintIndex())
if mibBuilder.loadTexts: policyConstraintIndex.setStatus('current')
policyConstraintPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 2), PolicyConstraintPolicyIndex())
if mibBuilder.loadTexts: policyConstraintPolicyIndex.setStatus('current')
policyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 3), PolicyIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyIndex.setStatus('current')
policyConstraintRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyConstraintRowStatus.setStatus('current')
policyConstraintNameTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3), )
if mibBuilder.loadTexts: policyConstraintNameTable.setStatus('current')
policyConstraintNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3, 1), ).setIndexNames((0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintIndex"))
if mibBuilder.loadTexts: policyConstraintNameEntry.setStatus('current')
policyConstraintName = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyConstraintName.setStatus('current')
policyConstraintNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 2, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyConstraintNameRowStatus.setStatus('current')
policyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3))
policyNextPolicyIndex = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 1), PolicyIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyNextPolicyIndex.setStatus('current')
policyTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2), )
if mibBuilder.loadTexts: policyTable.setStatus('current')
policyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1), ).setIndexNames((0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"))
if mibBuilder.loadTexts: policyEntry.setStatus('current')
policyName = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyName.setStatus('current')
requireNeNscOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("logicalAND", 2), ("logicalOR", 3))).clone('noop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: requireNeNscOperator.setStatus('current')
requireRpNscOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("logicalAND", 2), ("logicalOR", 3))).clone('noop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: requireRpNscOperator.setStatus('current')
mustAvoidNeNscOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("logicalAND", 2), ("logicalOR", 3))).clone('noop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mustAvoidNeNscOperator.setStatus('current')
policyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyRowStatus.setStatus('current')
policyNeNscTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3), )
if mibBuilder.loadTexts: policyNeNscTable.setStatus('current')
policyNeNscEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1), ).setIndexNames((0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"), (0, "ATM-POLICY-CONSTRAINT-MIB", "policyOperator"), (0, "ATM-POLICY-CONSTRAINT-MIB", "policyNeNscIndex"))
if mibBuilder.loadTexts: policyNeNscEntry.setStatus('current')
policyNeNscIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: policyNeNscIndex.setStatus('current')
policyOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 2), PolicyOperator())
if mibBuilder.loadTexts: policyOperator.setStatus('current')
policyNeNsc = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 3), NetworkEntityNetworkServiceCategory()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyNeNsc.setStatus('current')
policyNeNscRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyNeNscRowStatus.setStatus('current')
policyRpNscTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4), )
if mibBuilder.loadTexts: policyRpNscTable.setStatus('current')
policyRpNscEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1), ).setIndexNames((0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"), (0, "ATM-POLICY-CONSTRAINT-MIB", "policyRpNscIndex"))
if mibBuilder.loadTexts: policyRpNscEntry.setStatus('current')
policyRpNscIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: policyRpNscIndex.setStatus('current')
policyRpNsc = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1, 2), ResourcePartitionNetworkServiceCategory()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyRpNsc.setStatus('current')
policyRpNscRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyRpNscRowStatus.setStatus('current')
policyReferenceTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 5), )
if mibBuilder.loadTexts: policyReferenceTable.setStatus('current')
policyReferenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 5, 1), ).setIndexNames((0, "ATM-POLICY-CONSTRAINT-MIB", "policyIndex"), (0, "ATM-POLICY-CONSTRAINT-MIB", "policyConstraintIndex"))
if mibBuilder.loadTexts: policyReferenceEntry.setStatus('current')
policyReferencePCIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 3, 5, 1, 1), PolicyConstraintIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyReferencePCIndex.setStatus('current')
policyConstraintMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4))
policyConstraintMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 1))
policyConstraintMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 2))
policyConstraintMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 1, 1)).setObjects(("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintMIBMandatoryGroup"), ("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintMIBOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyConstraintMIBCompliance = policyConstraintMIBCompliance.setStatus('current')
policyConstraintMIBMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 2, 1)).setObjects(("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintMaximum"), ("ATM-POLICY-CONSTRAINT-MIB", "policyMaximum"), ("ATM-POLICY-CONSTRAINT-MIB", "policyNeNSCListMaximum"), ("ATM-POLICY-CONSTRAINT-MIB", "policyRpNSCListMaximum"), ("ATM-POLICY-CONSTRAINT-MIB", "policyIndex"), ("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintRowStatus"), ("ATM-POLICY-CONSTRAINT-MIB", "requireNeNscOperator"), ("ATM-POLICY-CONSTRAINT-MIB", "requireRpNscOperator"), ("ATM-POLICY-CONSTRAINT-MIB", "mustAvoidNeNscOperator"), ("ATM-POLICY-CONSTRAINT-MIB", "policyRowStatus"), ("ATM-POLICY-CONSTRAINT-MIB", "policyNeNsc"), ("ATM-POLICY-CONSTRAINT-MIB", "policyNeNscRowStatus"), ("ATM-POLICY-CONSTRAINT-MIB", "policyRpNsc"), ("ATM-POLICY-CONSTRAINT-MIB", "policyRpNscRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyConstraintMIBMandatoryGroup = policyConstraintMIBMandatoryGroup.setStatus('current')
policyConstraintMIBOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 5, 1, 1, 4, 2, 2)).setObjects(("ATM-POLICY-CONSTRAINT-MIB", "policyNextPolicyConstraintIndex"), ("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintName"), ("ATM-POLICY-CONSTRAINT-MIB", "policyConstraintNameRowStatus"), ("ATM-POLICY-CONSTRAINT-MIB", "policyNextPolicyIndex"), ("ATM-POLICY-CONSTRAINT-MIB", "policyName"), ("ATM-POLICY-CONSTRAINT-MIB", "policyReferencePCIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyConstraintMIBOptionalGroup = policyConstraintMIBOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("ATM-POLICY-CONSTRAINT-MIB", policyConstraintName=policyConstraintName, NetworkEntityNetworkServiceCategory=NetworkEntityNetworkServiceCategory, policyConstraintNameTable=policyConstraintNameTable, policyConstraintNameRowStatus=policyConstraintNameRowStatus, policyConstraintEntry=policyConstraintEntry, policyReferenceTable=policyReferenceTable, policyRpNscEntry=policyRpNscEntry, PolicyConstraintIndex=PolicyConstraintIndex, policyConstraintGroup=policyConstraintGroup, atmfSignalling=atmfSignalling, policyEntry=policyEntry, policyConstraintMIBConformance=policyConstraintMIBConformance, PolicyIndex=PolicyIndex, policyConstraintMIBOptionalGroup=policyConstraintMIBOptionalGroup, atmfPolicyConstraint=atmfPolicyConstraint, policyConstraintTable=policyConstraintTable, policyName=policyName, PolicyOperator=PolicyOperator, policyConstraintIndex=policyConstraintIndex, policyConstraintMIBMandatoryGroup=policyConstraintMIBMandatoryGroup, policyIndex=policyIndex, PolicyConstraintPolicyIndex=PolicyConstraintPolicyIndex, policyReferencePCIndex=policyReferencePCIndex, policyNeNscRowStatus=policyNeNscRowStatus, policyConstraintBaseGroup=policyConstraintBaseGroup, policyNextPolicyConstraintIndex=policyNextPolicyConstraintIndex, requireNeNscOperator=requireNeNscOperator, ResourcePartitionNetworkServiceCategory=ResourcePartitionNetworkServiceCategory, policyRpNscRowStatus=policyRpNscRowStatus, policyConstraintMIBCompliances=policyConstraintMIBCompliances, policyRpNscTable=policyRpNscTable, policyNeNSCListMaximum=policyNeNSCListMaximum, policyMaximum=policyMaximum, atmPolicyConstraintMIB=atmPolicyConstraintMIB, policyConstraintRowStatus=policyConstraintRowStatus, policyNextPolicyIndex=policyNextPolicyIndex, policyNeNscEntry=policyNeNscEntry, policyReferenceEntry=policyReferenceEntry, policyConstraintMIBGroups=policyConstraintMIBGroups, policyConstraintMIBCompliance=policyConstraintMIBCompliance, policyConstraintPolicyIndex=policyConstraintPolicyIndex, policyRpNscIndex=policyRpNscIndex, PYSNMP_MODULE_ID=atmPolicyConstraintMIB, mustAvoidNeNscOperator=mustAvoidNeNscOperator, requireRpNscOperator=requireRpNscOperator, atmForum=atmForum, policyConstraintMaximum=policyConstraintMaximum, policyTable=policyTable, policyNeNsc=policyNeNsc, policyNeNscTable=policyNeNscTable, policyOperator=policyOperator, policyNeNscIndex=policyNeNscIndex, policyConstraintMIBObjects=policyConstraintMIBObjects, policyRpNSCListMaximum=policyRpNSCListMaximum, policyRowStatus=policyRowStatus, atmForumNetworkManagement=atmForumNetworkManagement, policyGroup=policyGroup, policyRpNsc=policyRpNsc, policyConstraintNameEntry=policyConstraintNameEntry)
