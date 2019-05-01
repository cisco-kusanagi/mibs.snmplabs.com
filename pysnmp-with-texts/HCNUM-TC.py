#
# PySNMP MIB module HCNUM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HCNUM-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:04:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, ModuleIdentity, TimeTicks, Integer32, Bits, Counter64, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, Counter32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ModuleIdentity", "TimeTicks", "Integer32", "Bits", "Counter64", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "Counter32", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78))
hcnumTC.setRevisions(('2000-06-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hcnumTC.setRevisionsDescriptions(('Initial Version of the High Capacity Numbers MIB module, published as RFC 2856.',))
if mibBuilder.loadTexts: hcnumTC.setLastUpdated('200006080000Z')
if mibBuilder.loadTexts: hcnumTC.setOrganization('IETF OPS Area')
if mibBuilder.loadTexts: hcnumTC.setContactInfo(' E-mail: mibs@ops.ietf.org Subscribe: majordomo@psg.com with msg body: subscribe mibs Andy Bierman Cisco Systems Inc. 170 West Tasman Drive San Jose, CA 95134 USA +1 408-527-3711 abierman@cisco.com Keith McCloghrie Cisco Systems Inc. 170 West Tasman Drive San Jose, CA 95134 USA +1 408-526-5260 kzm@cisco.com Randy Presuhn BMC Software, Inc. Office 1-3141 2141 North First Street San Jose, California 95131 USA +1 408 546-1006 rpresuhn@bmc.com')
if mibBuilder.loadTexts: hcnumTC.setDescription('A MIB module containing textual conventions for high capacity data types. This module addresses an immediate need for data types not directly supported in the SMIv2. This short-term solution is meant to be deprecated as a long-term solution is deployed.')
class CounterBasedGauge64(TextualConvention, Counter64):
    description = "The CounterBasedGauge64 type represents a non-negative integer, which may increase or decrease, but shall never exceed a maximum value, nor fall below a minimum value. The maximum value can not be greater than 2^64-1 (18446744073709551615 decimal), and the minimum value can not be smaller than 0. The value of a CounterBasedGauge64 has its maximum value whenever the information being modeled is greater than or equal to its maximum value, and has its minimum value whenever the information being modeled is smaller than or equal to its minimum value. If the information being modeled subsequently decreases below (increases above) the maximum (minimum) value, the CounterBasedGauge64 also decreases (increases). Note that this TC is not strictly supported in SMIv2, because the 'always increasing' and 'counter wrap' semantics associated with the Counter64 base type are not preserved. It is possible that management applications which rely solely upon the (Counter64) ASN.1 tag to determine object semantics will mistakenly operate upon objects of this type as they would for Counter64 objects. This textual convention represents a limited and short-term solution, and may be deprecated as a long term solution is defined and deployed to replace it."
    status = 'current'

class ZeroBasedCounter64(TextualConvention, Counter64):
    description = 'This TC describes an object which counts events with the following semantics: objects of this type will be set to zero(0) on creation and will thereafter count appropriate events, wrapping back to zero(0) when the value 2^64 is reached. Provided that an application discovers the new object within the minimum time to wrap it can use the initial value as a delta since it last polled the table of which this object is part. It is important for a management station to be aware of this minimum time and the actual time between polls, and to discard data if the actual time is too long or there is no defined minimum time. Typically this TC is used in tables where the INDEX space is constantly changing and/or the TimeFilter mechanism is in use. Note that this textual convention does not retain all the semantics of the Counter64 base type. Specifically, a Counter64 has an arbitrary initial value, but objects defined with this TC are required to start at the value zero. This behavior is not likely to have any adverse effects on management applications which are expecting Counter64 semantics. This textual convention represents a limited and short-term solution, and may be deprecated as a long term solution is defined and deployed to replace it.'
    status = 'current'

mibBuilder.exportSymbols("HCNUM-TC", PYSNMP_MODULE_ID=hcnumTC, CounterBasedGauge64=CounterBasedGauge64, hcnumTC=hcnumTC, ZeroBasedCounter64=ZeroBasedCounter64)
