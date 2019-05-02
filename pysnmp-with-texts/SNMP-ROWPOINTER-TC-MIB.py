#
# PySNMP MIB module SNMP-ROWPOINTER-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-ROWPOINTER-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType, ObjectIdentity, Counter64, mib_2, TimeTicks, ModuleIdentity, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType", "ObjectIdentity", "Counter64", "mib-2", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpRowPointerTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67890))
snmpRowPointerTCMIB.setRevisions(('2000-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpRowPointerTCMIB.setRevisionsDescriptions(('Initial version, published as RFCnnnn.',))
if mibBuilder.loadTexts: snmpRowPointerTCMIB.setLastUpdated('200012180000Z')
if mibBuilder.loadTexts: snmpRowPointerTCMIB.setOrganization('SNMP Configuration WG')
if mibBuilder.loadTexts: snmpRowPointerTCMIB.setContactInfo('Bob Moore IBM Corporation, BRQA/502 PO Box 12195 Research Triangle Park, NC 27709, USA Phone: +1 919 254 4436 EMail: remoore@us.ibm.com Kwok Ho Chan Nortel Networks 600 Technology Park Drive Billerica, MA 01821, USA E-mail: khchan@nortelnetworks.com Send comments to snmpconf@ops.ietf.org.')
if mibBuilder.loadTexts: snmpRowPointerTCMIB.setDescription('This MIB module defines textual conventions similar to the RowPointer textual convention, with additional sementics.')
class StaticRowPointer(TextualConvention, ObjectIdentifier):
    description = 'Like a RowPointer, this textual convention represents a pointer to a conceptual row. The value is the name of the instance of the first accessible columnar object in the conceptual row. The additional semantics of this textual convention, relative to RowPointer, are related to the creation of instance-specific objects by cloning. The objects being cloned may either be special ones that express configuration information at the mechanism-specific level, or simply instance-specific ones that already exist at the time the cloning is done. When an object with the syntax StaticRowPointer is cloned, the StaticRowPointer in the newly cloned object is set to point to the same conceptual row that the StaticRowPointer in the cloned-from object pointed to. The cloning operations may be accomplished either with the script-based technique defined by SNMP Configuration, or by ordinary SNMP Get and Set operations. When cloning is not involved, this textual convention behaves identically to the RowPointer textual convention. Specifically, once an object with this syntax has been created, either by cloning or by other means, its value may be updated in the same way that the value of any other object with read-write or read-create access may be updated.'
    status = 'current'

mibBuilder.exportSymbols("SNMP-ROWPOINTER-TC-MIB", PYSNMP_MODULE_ID=snmpRowPointerTCMIB, StaticRowPointer=StaticRowPointer, snmpRowPointerTCMIB=snmpRowPointerTCMIB)
