#
# PySNMP MIB module VMWARE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Bits, TimeTicks, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Counter64, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "TimeTicks", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Counter64", "MibIdentifier", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwSystem, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwSystem")
vmwTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 1, 11))
vmwTcMIB.setRevisions(('2009-09-05 00:00', '2007-12-27 00:00',))
if mibBuilder.loadTexts: vmwTcMIB.setLastUpdated('200909050000Z')
if mibBuilder.loadTexts: vmwTcMIB.setOrganization('VMware, Inc')
class VmwSubsystemTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 1), ("chassis", 2), ("powerSupply", 3), ("fan", 4), ("cpu", 5), ("memory", 6), ("battery", 7), ("temperatureSensor", 8), ("raidController", 9), ("voltage", 10))

class VmwCIMAlertTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("communications", 2), ("qos", 3), ("processingError", 4), ("deviceAlert", 5), ("environmentalAlert", 6), ("modelChange", 7), ("securityAlert", 8))

class VmwCIMAlertFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("cimObjectPath", 2))

class VmwSubsystemStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("marginal", 3), ("critical", 4), ("failed", 5))

class VmwCIMSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("information", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6), ("fatal", 7))

class VmwCimName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VmwConnectedState(TextualConvention, OctetString):
    status = 'current'
    displayHint = '7a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 7)

class VmwLongDisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'

class VmwLongSnmpAdminString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4096t'

mibBuilder.exportSymbols("VMWARE-TC-MIB", VmwSubsystemStatus=VmwSubsystemStatus, VmwLongSnmpAdminString=VmwLongSnmpAdminString, VmwSubsystemTypes=VmwSubsystemTypes, vmwTcMIB=vmwTcMIB, VmwCIMSeverity=VmwCIMSeverity, PYSNMP_MODULE_ID=vmwTcMIB, VmwConnectedState=VmwConnectedState, VmwCimName=VmwCimName, VmwCIMAlertFormat=VmwCIMAlertFormat, VmwCIMAlertTypes=VmwCIMAlertTypes, VmwLongDisplayString=VmwLongDisplayString)
