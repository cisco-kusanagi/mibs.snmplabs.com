#
# PySNMP MIB module SNMP-CONFIGURATION-TCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-CONFIGURATION-TCS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ModuleIdentity, Bits, Counter64, mib_2, Gauge32, Unsigned32, IpAddress, MibIdentifier, ObjectIdentity, iso, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "mib-2", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "ObjectIdentity", "iso", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpConfigurationTCsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67890))
snmpConfigurationTCsMIB.setRevisions(('2000-11-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpConfigurationTCsMIB.setRevisionsDescriptions(('Initial version, published as RFCnnnn.',))
if mibBuilder.loadTexts: snmpConfigurationTCsMIB.setLastUpdated('200011140000Z')
if mibBuilder.loadTexts: snmpConfigurationTCsMIB.setOrganization('SNMP Configuration WG')
if mibBuilder.loadTexts: snmpConfigurationTCsMIB.setContactInfo('Bob Moore IBM Corporation, BRQA/502 PO Box 12195 Research Triangle Park, NC 27709, USA Phone: +1 919 254 4436 EMail: remoore@us.ibm.com Kwok Ho Chan Nortel Networks 600 Technology Park Drive Billerica, MA 01821, USA E-mail: khchan@nortelnetworks.com Send comments to smnpconf@ops.ietf.org.')
if mibBuilder.loadTexts: snmpConfigurationTCsMIB.setDescription('This MIB module defines textual conventions useful for policy-based configuration using SNMP.')
class DynamicRowPointer(TextualConvention, ObjectIdentifier):
    description = 'Like a RowPointer, this textual convention represents a pointer to a conceptual row. The value is the name of the instance of the first accessible columnar object in the conceptual row. The additional semantics of this textual convention, relative to RowPointer, are related to the creation of instance-specific objects by cloning. The objects being cloned may either be special ones that express configuration information at the implementation-specific level, or simply instance-specific ones that already exist at the time the cloning is done. When an object with the syntax DynamicRowPointer is cloned, a new conceptual row is created based on the conceptual row pointed to by the DynamicRowPointer in the cloned-from object, and the DynamicRowPointer in the newly cloned object is set to point to this new conceptual row. The cloning operations may be accomplished either with the script-based technique defined by SNMP Configuration, or by ordinary SNMP Get and Set operations. When cloning is not involved, this textual convention behaves identically to the RowPointer textual convention. Specifically, once an object with this syntax has been created, either by cloning or by other means, its value may be updated in the same way that the value of any other object with read-write or read-create access may be updated.'
    status = 'current'

class StaticRowPointer(TextualConvention, ObjectIdentifier):
    description = 'Like a RowPointer, this textual convention represents a pointer to a conceptual row. The value is the name of the instance of the first accessible columnar object in the conceptual row. The additional semantics of this textual convention, relative to RowPointer, are related to the creation of instance-specific objects by cloning. The objects being cloned may either be special ones that express configuration information at the implementation-specific level, or simply instance-specific ones that already exist at the time the cloning is done. When an object with the syntax StaticRowPointer is cloned, the StaticRowPointer in the newly cloned object is set to point to the same conceptual row that the StaticRowPointer in the cloned-from object pointed to. The cloning operations may be accomplished either with the script-based technique defined by SNMP Configuration, or by ordinary SNMP Get and Set operations. When cloning is not involved, this textual convention behaves identically to the RowPointer textual convention. Specifically, once an object with this syntax has been created, either by cloning or by other means, its value may be updated in the same way that the value of any other object with read-write or read-create access may be updated.'
    status = 'current'

mibBuilder.exportSymbols("SNMP-CONFIGURATION-TCS-MIB", DynamicRowPointer=DynamicRowPointer, snmpConfigurationTCsMIB=snmpConfigurationTCsMIB, PYSNMP_MODULE_ID=snmpConfigurationTCsMIB, StaticRowPointer=StaticRowPointer)
